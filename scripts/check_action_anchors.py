"""Audit a frame-based GMV plan without modifying media/projects.

Uses the research plan schema: delivery_fps, duration_frames, music.source_start_s,
shots (id, in_frame, out_frame_exclusive, capture_fps, source_time_keys), events
(delivery_frame, source_id, source_target_s, music_source_candidate_s).
This verifies arithmetic/coverage, not contact classification or perceived rhythm.
"""
import argparse,json,sys
from pathlib import Path

def interpolate(keys,frame):
 for a,b in zip(keys,keys[1:]):
  if a['delivery_frame']<=frame<=b['delivery_frame']:
   q=(frame-a['delivery_frame'])/(b['delivery_frame']-a['delivery_frame'])
   return a['source_s']+q*(b['source_s']-a['source_s'])
 raise ValueError('Action frame is outside source-time keys')

def audit(plan):
 fps=float(plan['delivery_fps']);duration=plan['duration_frames'];assert fps>0 and isinstance(duration,int)and duration>0
 shots=plan['shots'];assert shots,'No shots';cursor=0;byid={};speeds=[];warnings=[]
 for s in shots:
  a=s['in_frame'];b=s['out_frame_exclusive'];assert isinstance(a,int)and isinstance(b,int)and a==cursor and b>a,('Gap/overlap/invalid boundary',s['id'],cursor,a,b)
  cursor=b;assert s['id']not in byid,'Use unique shot instance IDs if one media source appears twice';byid[s['id']]=s
  keys=s['source_time_keys'];assert len(keys)>=2 and keys[0]['delivery_frame']<=a and keys[-1]['delivery_frame']>=b,('Missing source-time handles',s['id'])
  capture=float(s.get('capture_fps',0));floor=fps/capture if capture else None
  for x,y in zip(keys,keys[1:]):
   delta=y['delivery_frame']-x['delivery_frame'];assert delta>0 and y['source_s']>=x['source_s']>=0,('Non-monotonic keys',s['id'])
   speed=(y['source_s']-x['source_s'])/(delta/fps);item={'shot':s['id'],'frame_range':[x['delivery_frame'],y['delivery_frame']],'speed':speed,'capture_speed_floor':floor};speeds.append(item)
   if floor and speed<floor-1e-5:warnings.append({'shot':s['id'],'range':item['frame_range'],'reason':'Hold or speed below capture sampling floor; repeated/generated frames need explicit review.'})
 assert cursor==duration,('Coverage does not equal duration',cursor,duration)
 result=[]
 for e in plan['events']:
  frame=e['delivery_frame'];assert isinstance(frame,int)and 0<=frame<duration
  r={'label':e['label'],'frame':frame,'offset_to_music_candidate_ms':1000*(plan['music']['source_start_s']+frame/fps-e['music_source_candidate_s'])}
  sid=e.get('source_id')
  if sid:
   s=byid[sid];assert s['in_frame']<=frame<s['out_frame_exclusive'],('Action belongs to inactive shot',e)
   actual=interpolate(s['source_time_keys'],frame);target=e['source_target_s'];r['mapped_source_s']=actual;r['target_source_s']=target;r['source_anchor_error_s']=actual-target
   assert abs(actual-target)<1e-5,('Action anchor differs from declared source target',r)
  result.append(r)
 return {'plan_arithmetic_passed':True,'coverage_frames':duration,'fps':fps,'speeds':speeds,'events':result,'warnings':warnings,'native_render_verified':False,'perceived_rhythm_verified':False,'note':'Native import/encode audio offset is measured from output separately. Candidate offsets omit unmeasured onset and action uncertainty.'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('plan',type=Path);args=p.parse_args()
 try:result=audit(json.loads(args.plan.read_text(encoding='utf-8-sig')))
 except(AssertionError,KeyError,ValueError,TypeError)as e:print(json.dumps({'plan_arithmetic_passed':False,'error':str(e)}));return 1
 print(json.dumps(result,ensure_ascii=False,indent=2));return 0
if __name__=='__main__':sys.exit(main())
