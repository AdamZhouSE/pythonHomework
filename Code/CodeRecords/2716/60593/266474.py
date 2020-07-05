import sys
_=input()
lines=sys.stdin.readlines()
grid=[]
for line in lines:
    line=line.strip().reaplace(',','')
    grid.append(line)
print(grid)    