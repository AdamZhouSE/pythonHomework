m,n=map(int,input().split())
a=input()
b=input()
res=[]
for i in range(n-m+1):
    tem=b[i:i+m]
    check=True
    for j in range(m):
        if a[j]!="*" and tem[j]!="*":
            if a[j]!=tem[j]:
                check=False
                break
    if check:
        res.append(i+1)
print(len(res))
if len(res)>0:
    print(' '.join(str(i) for i in res),end=" ")
    print()