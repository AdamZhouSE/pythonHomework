import sys


a=[]
lines=sys.stdin.readlines()[1:-1]
for i in range(len(lines)-1):
    a.append(eval(lines[i][2:-2]))
a.append(eval(lines[-1][2:-1]))  
print(a)
