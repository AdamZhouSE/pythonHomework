import math
def find(a):
    temp=[]
    for i in range(1,(1+a)*a//2+1):
        temp.append(i)
    i=0
    num=0
    k=0
    while i<=len(temp):
        sub=[]
        cons=1
        sub=temp[i:i+k+1]
        if i==0:
            cons=1
        else:
            for h in sub:
                cons=cons*h
        num+=cons
        k=k+1
        i+=k
    return num


b=int(input())
CONS=[]
final=[]
for i in range(b):
    CONS.append(int(input()))
for i in CONS:
    final.append(find(i)-1)
for i in final:
    print(i)
