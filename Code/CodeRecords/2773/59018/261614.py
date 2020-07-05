import sys


a=[]
lines=sys.stdin.readlines()[1:-1]
print(lines)
print(len(lines))
for i in lines:
    if i!=' ':    
        a.append(i)
print(a)