k,m=map(int,input().split())
s=' '+input()
n=int(input())
a,b,c=[0]*(n+1),[0]*(n+1),[0]*(n+1)
ans=[0]*220
for i in range(1,n+1):
    a[i],b[i],c[i]=map(int,input().split())
for i in range(1,k+1):
    ans[i]=i
for i in range(n,-1,-1):
    for j in range(1,k+1):
        if(ans[j]<=c[i]):
            continue
        if(ans[j]<=c[i]+b[i]-a[i]):
            ans[j]=ans[j]-c[i]+a[i]
        else:
            ans[j]-=b[i]-a[i]
for i in range(1,k+1):
    print(s[ans[i]],end='')