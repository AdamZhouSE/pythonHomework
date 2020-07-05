n=int(input())
m=int(input())
res=n//m
if n*m<0:
    res=res+1
print(res)