n,d=map(int,input().split())
f=[0]*(d+1)
for i in range(1,d+1):
    f[i]=f[i-1]**n+1
print(f[i]-f[i-1])