import sys
delS=input()
_=[]
lines=sys.stdin.readlines()
for line in lines:
    _.append(line.replace(delS,'').replace(' ',''))
for __ in _:
    print(__,end='')