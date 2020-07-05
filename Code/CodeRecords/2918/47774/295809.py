n=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
h=[0 for i in range(100)]
t=-1
for i in range(n):
    t=max(a[i],t)
    h[a[i]]+=1
ans=0
while n:
    cnt=0
    for i in range(t+1):
        while h[i] and i>=cnt:
            h[i]-=1
            cnt+=1
            n-=1
    ans+=1
print(ans)