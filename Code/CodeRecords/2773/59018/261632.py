import sys


a=[]
lines=sys.stdin.readlines()[1:-1]
print(lines)
print(lines[0][0])
print(len(lines[0]))
for i in range(len(lines)-1):
    a.append(lines[i][2:-2])
a.append(lines[-1][2:-1])    
print(type(a[0]))