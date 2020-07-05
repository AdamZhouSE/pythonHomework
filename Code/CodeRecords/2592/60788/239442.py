from sys import stdin
import cmath

def f(s):
    b=0
    i=1
    while True:
        if i>=2*s:
            break
        max=int(2*cmath.sqrt(s*s-i*i/4).real)
        if max>=1:
            b+=int(max)
        else:
            break
        i+=1
    return b
    
    
    
num=int(stdin.readline().strip())
for i in range(0,num):
    a=int(stdin.readline().strip())
    print(f(a))