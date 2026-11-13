"""src/template.html + src/data.js + src/geo_min.js -> index.html (and the workshop copy)"""
import os, shutil
here=os.path.dirname(os.path.abspath(__file__))
rd=lambda p: open(os.path.join(here,'src',p),encoding='utf-8').read()
t=rd('template.html').replace('/*__DATA__*/',rd('data.js')).replace('/*__AREAS__*/',rd('areas.js')).replace('/*__KOREA__*/',rd('geo_min.js'))
out=os.path.join(here,'index.html')
open(out,'w',encoding='utf-8').write(t)
shutil.copyfile(out,os.path.join(here,'..','개발계획_지도.html'))
print('built',len(t))
