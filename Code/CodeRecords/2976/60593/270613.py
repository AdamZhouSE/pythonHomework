import sys
import re
delS=input()
_=[]
lines=sys.stdin.readlines()
for line in lines:
    _.append(re.sub(delS,'',line,flags=re.I).replace(' ',''))
for __ in _:
    print(__,end='')