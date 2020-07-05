n=int(input())
l=list(map(int,input().split()))
l.sort()
half=len(l)//2
res=l[:half]
a=sum(res)
b=sum(l)-sum(res)
print(a*a+b*b)