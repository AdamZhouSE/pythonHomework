n=int(input())
data=list(map(int,input().split()))
maxValue=max(data)
cnt=[0]*100050
f=[0]*100050
for i in range(n):
    temp=data[i]
    cnt[temp]+=1
f[1]=cnt[1]
for i in range(2,maxValue+1):
    f[i]=max(f[i-1],f[i-2]+i*cnt[i])
print(f[maxValue])