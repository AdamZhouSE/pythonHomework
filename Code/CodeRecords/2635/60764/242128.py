n=int(input())
a=1
while a<n:
    a=5*a+1
res=5
while a>1:
    if a-1==n:
        res=0
        break
    a=int((a-1)/5)
    n=n%a
print(res)