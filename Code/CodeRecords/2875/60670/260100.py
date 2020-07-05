n=int(input())
dic={}
a=list(map(int,input().split()))
for i in range(0,n):
    dic[a[i]]=i
ans=""
for i in range(0,n):
    ans=ans+str(dic[i])+" "
print(ans[0:len(ans)-1])