n=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
ss=input()
b=[int(i) for i in ss.split(' ')]
arr=[0 for i in range(n*2)]
for i in range(n):
    arr[b[i]]=i+1
flag,ans=0,0
for i in range(n):
    k=arr[a[i]]
    m=k-flag-1
    if m<0:
        continue
    ans+=m
    flag=k
print(ans)