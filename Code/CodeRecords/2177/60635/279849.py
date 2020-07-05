k=int(input())
n=k+1
print(n)
l=0
r=n+1
ans=[0]*(n+1)
for i in range(n,0,-1):
    if (n+1-i)&1:
        r-=1
        ans[i]=r
    else:
        l+=1
        ans[i]=l
print(*ans[1:],end=' ')