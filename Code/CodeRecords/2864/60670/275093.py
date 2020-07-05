n=int(input())
a=list(map(int,input().split()))
maxn=max(a)
count=[0 for i in range(0,maxn+1)]
for i in a:
    count[i]+=i
f=[0 for i in range(0,maxn+1)]
f[1]=count[1]
for i in range(2,maxn+1):
    f[i]=max(f[i-1],f[i-2]+count[i])
print(f[maxn])