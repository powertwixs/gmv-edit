"""Portable, source-read-only every-frame contact sheet with actual source PTS.
Requires ffmpeg, ffprobe, Pillow. Does not listen to audio or classify cuts.
"""
import argparse,hashlib,json,math,re,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

def run(args):
 r=subprocess.run(args,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr.decode(errors='replace')[-2000:])
 return r

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--start',type=float,required=True);p.add_argument('--frames',type=int,default=24);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 src=a.input.resolve();out=a.output.resolve()
 if not src.is_file():p.error('Input file missing')
 if a.frames<2 or a.frames>240:p.error('Choose 2 to 240 consecutive frames for readable review')
 if a.start<0:p.error('Start must be nonnegative')
 if out==src or out in src.parents:p.error('Output must be a separate new derived folder')
 if out.exists()and any(out.iterdir()):p.error('Output folder is not empty; choose another version')
 out.mkdir(parents=True,exist_ok=True);before=src.stat()
 with src.open('rb')as f:
  first=f.read(1048576);f.seek(max(0,before.st_size-1048576));last=f.read(1048576)
 fp=hashlib.sha256(first+last+str(before.st_size).encode()).hexdigest()
 probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(src)]).stdout)
 r=run(['ffmpeg','-v','info','-threads','2','-copyts','-ss',str(a.start),'-i',str(src),'-an','-frames:v',str(a.frames),'-vf','scale=320:-2,showinfo','-fps_mode','passthrough','-threads','1',str(out/'frame_%04d.jpg')])
 pts=[float(x)for x in re.findall(r' n:\s*\d+.*?pts_time:([\d.eE+-]+)',r.stderr.decode(errors='replace'))][:a.frames];frames=sorted(out.glob('frame_*.jpg'))
 if len(pts)!=len(frames)or len(frames)<2:raise RuntimeError('Insufficient frames or missing PTS; do not infer frame positions')
 if src.stat().st_size!=before.st_size or src.stat().st_mtime_ns!=before.st_mtime_ns:raise RuntimeError('Source changed during inspection; evidence is stale')
 try:font=ImageFont.truetype('DejaVuSans.ttf',15)
 except OSError:font=ImageFont.load_default()
 h=Image.open(frames[0]).height;cols=6;cell=h+25;sheet=Image.new('RGB',(cols*320,math.ceil(len(frames)/cols)*cell),(14,16,23));d=ImageDraw.Draw(sheet)
 for i,(f,t)in enumerate(zip(frames,pts)):
  x=i%cols*320;y=i//cols*cell;sheet.paste(Image.open(f),(x,y));d.text((x+3,y+h+3),f'{t:.6f}s source PTS',font=font,fill='white')
 sheet.save(out/'EveryFrame.jpg',quality=93)
 v=next(s for s in probe['streams']if s['codec_type']=='video');result={'source':str(src),'fingerprint':fp,'requested_start':a.start,'requested_frames':a.frames,'actual_frames':len(frames),'source_pts':pts,'fps_nominal':v['r_frame_rate'],'fps_average':v['avg_frame_rate'],'audio_start':[s.get('start_time')for s in probe['streams']if s['codec_type']=='audio'],'frames_are_consecutive':True,'visual_reviewed':False,'audio_reviewed':False,'sheet':str(out/'EveryFrame.jpg')}
 (out/'evidence.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps({'frames':len(frames),'pts_first':pts[0],'pts_last':pts[-1],'sheet':result['sheet']},ensure_ascii=False))
if __name__=='__main__':main()
