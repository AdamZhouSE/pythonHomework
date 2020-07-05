mn=list(input())
m=int(mn[1])
n=int(mn[3])
res=m
for x in range(m+1,n+1):
    res=res&x
print(res)
