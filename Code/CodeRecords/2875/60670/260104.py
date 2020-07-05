n=int(input())
dic={}
a=list(map(int,input().split()))
for i in range(0,n):
    dic[a[i]]=i+1
ans=""
for i in range(1,n+1):
    ans=ans+str(dic[i])+" "
print(ans[0:len(ans)-1])