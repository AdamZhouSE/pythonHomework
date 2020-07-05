import math

def depth(n):
    res=0
    while n>0:
        n=int(n/2)
        res+=1
    return res


n=int(input())
res=''
l=depth(n)
while l>0:
    res=str(n)+' '+res
    if l%2==0:
        n=int(math.pow(2,l))+int(math.pow(2,l-1))-1-n
        n = int(n / 2)
        l=l-1
    else:
        n=int(n/2)
        l=l-1
        n = int(math.pow(2, l)) + int(math.pow(2, l - 1)) - 1 - n

a=res[:-1].split()
for i in range(0,len(a)):
    a[i]=int(a[i])
print(a)
