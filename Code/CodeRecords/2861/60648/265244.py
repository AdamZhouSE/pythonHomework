n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
r=0
for i in range(n):
    minn=10000000
    for j in range(n):
        if i!=j:
            if abs(ls[i]-ls[j])<minn:
                minn=abs(ls[i]-ls[j])
    r+=minn
    
if r==2:
    print(2)
else:
    print(r//2)