n=int(input())
happy=[]
f=[]
for i in range(0,9000):
    f.append([0,0])

for i in range(1,n+1):
    f[i][1]=int(input())
ans=f[1][1]
for i in range(1,n+1):
    nums=list(map(int,input().split(" ")))
    a=nums[0]
    b=nums[1]
    f[b][1]+=f[a][0]
    f[b][0] += max(f[a][0], f[a][1])
    ans = max(ans, f[b][1])
    ans = max(ans, f[b][0])

print(ans)