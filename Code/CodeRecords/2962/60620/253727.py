n,p=map(int,input().split())
a=list(map(str,input().split()))
result=[]
for i in range(n):
    x=((ord(a[i][-3])-65)*32**2+(ord(a[i][-2])-65)*32+ord(a[i][-1])-65)%p
    if x in result:
        num=1
        y=(x+num**2)%p
        if y in result:y=6
        result.append(y)
    else:
        result.append(x)
print(*result)