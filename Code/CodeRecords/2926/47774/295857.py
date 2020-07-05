n=int(input())
ss=input()
a=[int(i) for i in ss.split(' ')]
arr=[0 for i in range(2*100)]
for i in a:
    arr[i]+=1
ans=-1
for i in range(101):
    ans=max(ans,arr[i])
print(ans)