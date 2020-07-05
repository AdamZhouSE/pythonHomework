import sys


a=[]
lines=sys.stdin.readlines()[1:-1]
print(lines)
for i in lines:
    a.append(i)
print(a)