from sys import stdin
def is_deficient(s):
    t=0
    li=find_divisor(s)
    for i in li:
        t+=i
    return t<2*s  

def find_divisor(s):
    t=[]
    for i in range(1,s+1):
        if s%i==0:
            t.append(i)
    return t
   
num=int(stdin.readline().strip())
for i in range(0,num):
    a=int(stdin.readline().strip())
    if is_deficient(a):
        print(1)
    else:
        print(0)