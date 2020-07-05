n,k=map(int,input().split())
arr=map(int,input().split())
temp=0
for i in arr:
    if k%i==0:
        if i>temp:
            temp=i
            ans=int(k/i)
print(ans)