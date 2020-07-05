import math

def dfs(num,deep,t):
    if v[num]==1:return 0
    if deep==t:return 1
    v[num]=1
    ans[deep]=num%2
    if dfs((num*2)%t,deep+1,t): return 1
    if dfs((num*2+1)%t,deep+1,t):return 1
    v[num]=0
    return 0

n=int(input())
t=1
v=[0 for i in range(int(math.pow(2,n)))]
ans=[0 for i in range(int(math.pow(2,n)))]
for i in range(n):
    t*=2
print(t,end=' ')
dfs(0,1,t)
for i in range(1,n):print(0,end='')
for i in range(1,t-n+2):print(ans[i],end='')
print()