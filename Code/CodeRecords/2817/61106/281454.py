n=int(input())
f=list(map(int,input().split()))
for i in range(n):
    if (f[f[f[i]-1]-1]-1==i):
        result=true
    else:
        result=false 
if result:
    print('YES')
else:
    print('NO')