"""Audit explicitly marked image regions/attention points; never detect gaze or grade footage.

python region_continuity.py PLAN.json --output NEW_FOLDER
Requires Pillow. Rectangles and points use normalized coordinates inside analysis_box.
"""
import argparse,json,math
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageStat

def rect(v,label):
 if not isinstance(v,list)or len(v)!=4 or not all(isinstance(x,(int,float))and math.isfinite(x)for x in v):raise ValueError(label+' must be four finite numbers')
 if not(0<=v[0]<v[2]<=1 and 0<=v[1]<v[3]<=1):raise ValueError(label+' must be ordered within0..1')
 return v

def pixels(v,w,h):
 box=tuple(round(x*n)for x,n in zip(v,[w,h,w,h]))
 if box[2]<=box[0]or box[3]<=box[1]:raise ValueError('Region rounds to an empty pixel box')
 return box

def stats(im):
 rgb=ImageStat.Stat(im).mean[:3]
 return{'mean_encoded_rgb_255':rgb,'weighted_encoded_brightness_proxy_255':sum(c*w for c,w in zip(rgb,[.2126,.7152,.0722])),'mean_rgb_channel_range':max(rgb)-min(rgb)}

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('plan',type=Path);parser.add_argument('--output',type=Path,required=True);a=parser.parse_args();plan=json.loads(a.plan.read_text(encoding='utf-8-sig'));out=a.output.resolve()
 if out.exists():raise ValueError('Output exists; choose a new folder')
 entries=[];ids=set();pictures=[]
 for f in plan['frames']:
  ident=f['id']
  if ident in ids:raise ValueError('Duplicate frame id: '+ident)
  ids.add(ident);path=Path(f['image']);path=path if path.is_absolute()else a.plan.resolve().parent/path
  box=rect(f.get('analysis_box',[0,0,1,1]),'analysis_box');focus=f['focus']
  if not isinstance(focus,list)or len(focus)!=2 or not all(isinstance(x,(int,float))and math.isfinite(x)and 0<=x<=1 for x in focus):raise ValueError('focus must be two finite normalized values')
  with Image.open(path)as original:
   dims=original.size;icc=bool(original.info.get('icc_profile'));im=original.convert('RGB').crop(pixels(box,*dims))
  values=[];drawing=im.copy();d=ImageDraw.Draw(drawing)
  for region in f.get('regions',[]):
   rp=pixels(rect(region['rect'],'region '+region['name']),*im.size);values.append(dict(name=region['name'],normalized_rect=region['rect'],pixel_rect=rp,**stats(im.crop(rp))));d.rectangle(rp,outline=(80,250,110),width=max(1,im.width//400));d.text((rp[0],rp[1]),region['name'],fill=(255,255,255))
  x,y=focus[0]*im.width,focus[1]*im.height;r=max(4,im.width//80);d.line((x-r,y,x+r,y),fill=(255,90,90),width=max(1,im.width//400));d.line((x,y-r,x,y+r),fill=(255,90,90),width=max(1,im.width//400))
  entries.append({'id':ident,'image':str(path.resolve()),'source_dimensions':dims,'icc_present_not_applied':icc,'analysis_box':box,'manual_focus_normalized':focus,'manual_focus_label':f.get('focus_label','unspecified'),'whole_analysis_area':stats(im),'regions':values});pictures.append(drawing)
 comparisons=[];byid={f['id']:f for f in entries}
 for t in plan.get('transitions',[]):
  one,two=byid[t['from']],byid[t['to']];distance=math.dist(one['manual_focus_normalized'],two['manual_focus_normalized']);common={r['name']:r for r in one['regions']};deltas=[]
  for region in two['regions']:
   if region['name']in common:deltas.append({'region':region['name'],'encoded_brightness_proxy_delta_255':region['weighted_encoded_brightness_proxy_255']-common[region['name']]['weighted_encoded_brightness_proxy_255']})
  comparisons.append({'from':t['from'],'to':t['to'],'manual_focus_normalized_distance':distance,'same_named_region_deltas':deltas,'editor_reason':t.get('reason',''),'automatic_quality_grade':None})
 if not entries:raise ValueError('No frames supplied')
 out.mkdir(parents=True);pages=[];font=ImageFont.load_default()
 for base in range(0,len(entries),8):
  sheet=Image.new('RGB',(4*480,2*300),(12,15,22));d=ImageDraw.Draw(sheet)
  for j,(entry,im)in enumerate(zip(entries[base:base+8],pictures[base:base+8])):
   im.thumbnail((480,270));x=j%4*480;y=j//4*300;sheet.paste(im,(x+(480-im.width)//2,y+(270-im.height)//2));d.text((x+4,y+274),entry['id'],font=font,fill='white')
  path=out/f'Regions_Page_{base//8+1}.jpg';sheet.save(path,quality=95);pages.append(str(path))
 report={'frames':entries,'comparisons':comparisons,'boards':pages,'manual_annotations_visually_verified':False,'limits':'Explicit editor annotations only, not eye tracking, face/skin detection or automatic color matching. Encoded RGB proxy is not linear luminance, IRE, exposure, calibrated color or skin accuracy. Embedded ICC is recorded but not applied. Same-named regions can differ in subject/lighting; inspect them. Analysis boxes must deliberately exclude bars/irrelevant canvas.'}
 (out/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps({'report':str(out/'report.json'),'boards':pages,'frames':len(entries),'comparisons':len(comparisons)},ensure_ascii=False))
if __name__=='__main__':main()
