import sys
_=input()
lines=sys.stdin.readlines()
grid=[]
for line in lines:
    if(line==']'):
        break
    line=line.strip().replace(',','').replace('"','')
    grid.append(line)
print(grid)    