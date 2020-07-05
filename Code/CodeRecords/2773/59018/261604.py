import sys


a=[]
lines=sys.stdin.readlines()[1:-1]
print(lines)
for i in range(len(lines)):
    a.append(list(lines[i][0:-1]))
print(a)