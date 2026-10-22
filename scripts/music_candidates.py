"""Generate unverified percussive attack and tempo candidates from supplied music.
Requires ffmpeg, ffprobe, NumPy and SciPy. No downloads, source changes or listening claims.
"""
import argparse,hashlib,json,subprocess
from pathlib import Path
import numpy as np
from scipy import signal,ndimage
from scipy.io import wavfile

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--start',type=float,default=0);p.add_argument('--duration',type=float);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 src=a.input.resolve();out=a.output.resolve()
 if not src.is_file()or a.start<0 or(a.duration is not None and a.duration<=0):p.error('Valid input and nonnegative start / positive duration required')
 if out==src or out in src.parents:p.error('Output must be a separate derived folder')
 if out.exists()and any(out.iterdir()):p.error('Output folder is not empty; choose another version')
 out.mkdir(parents=True,exist_ok=True);st=src.stat()
 def run(cmd):
  r=subprocess.run(cmd,capture_output=True)
  if r.returncode:raise RuntimeError(r.stderr.decode(errors='replace')[-1800:])
  return r
 probe=json.loads(run(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(src)]).stdout)
 with src.open('rb')as f:
  first=f.read(1048576);f.seek(max(0,st.st_size-1048576));last=f.read(1048576)
 fp=hashlib.sha256(first+last+str(st.st_size).encode()).hexdigest()
 cmd=['ffmpeg','-v','error','-threads','2','-ss',str(a.start),'-i',str(src)]
 if a.duration is not None:cmd+=['-t',str(a.duration)]
 cmd+=['-vn','-ac','1','-ar','24000','-c:a','pcm_s16le',str(out/'audio_24k.wav')];run(cmd)
 sr,x=wavfile.read(out/'audio_24k.wav');x=x.astype(np.float32)/32768
 if len(x)<24000:raise RuntimeError('Use at least one second of audio')
 f,t,z=signal.stft(x,sr,nperseg=1024,noverlap=784,boundary=None);mag=np.abs(z)
 harmonic=ndimage.median_filter(mag,size=(1,31));perc=ndimage.median_filter(mag,size=(17,1));pmag=mag*perc**2/(perc**2+harmonic**2+1e-12)
 def flux(low,high):
  m=pmag[(f>=low)&(f<=high)];log=np.log1p(m*500);y=np.maximum(np.diff(log,axis=1,prepend=log[:,:1]),0).sum(axis=0);y=ndimage.gaussian_filter1d(y,.7);return y/(np.percentile(y,96)+1e-8)
 kick=flux(35,160);snare=flux(600,6000);rms=np.sqrt(np.maximum(0,ndimage.uniform_filter1d(x*x,1200)[::240]))[:len(t)]
 def attacks(y):
  peaks,_=signal.find_peaks(y,distance=13,prominence=.45,height=.65)
  return [{'decoded_relative_s':round(float(t[i]),6),'requested_source_s':round(float(t[i]+a.start),6),'strength':round(float(y[i]),3)}for i in peaks]
 env=.7*np.minimum(3,kick)+.3*np.minimum(3,snare);ac=signal.correlate(env-env.mean(),env-env.mean(),method='fft')[len(env)-1:];scores=[]
 for bpm in np.arange(70,180.01,.1):
  lag=round(6000/bpm)
  if 4*lag<len(ac):scores.append((float(ac[lag]+.5*ac[2*lag]+.25*ac[4*lag]),float(bpm)))
 top=[]
 for score,bpm in sorted(scores,reverse=True):
  if all(abs(bpm-v['bpm'])>2 for v in top):top.append({'bpm':round(bpm,2),'autocorrelation_score':score})
  if len(top)==5:break
 if src.stat().st_size!=st.st_size or src.stat().st_mtime_ns!=st.st_mtime_ns:raise RuntimeError('Source changed; analysis is stale')
 np.savez_compressed(out/'features.npz',decoded_relative_time=t,kick=kick,snare=snare,rms=rms)
 result={'source':str(src),'fingerprint':fp,'requested_seek_s':a.start,'duration_decoded_s':len(x)/sr,'sample_rate':sr,'fft_samples':1024,'hop_samples':240,'timing_warning':'FFT windows, HPSS, codecs and demux seek may shift timing. Requested-source time is provisional; reconcile container and audio start PTS before sync claims.','container_start':probe['format'].get('start_time'),'audio_start':[s.get('start_time')for s in probe['streams']if s['codec_type']=='audio'],'audio_listened':False,'tempo_verified':False,'tempo_candidates':top,'kick_candidates':attacks(kick),'snare_candidates':attacks(snare)}
 (out/'candidates.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps({'duration_s':result['duration_decoded_s'],'low_attack_candidates':len(result['kick_candidates']),'high_attack_candidates':len(result['snare_candidates']),'tempo_candidates':top[:2]},ensure_ascii=False))
if __name__=='__main__':main()
