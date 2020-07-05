n=int(input())
a=input().split()
b="".join(a)
num1=a.count('1')-1
beg=b.find('1')
res=1
nex=-1
while num1>0:
    nex=b.find('1',beg+1)
    res*=nex-beg
    num1-=1
    beg=nex
print(res)


