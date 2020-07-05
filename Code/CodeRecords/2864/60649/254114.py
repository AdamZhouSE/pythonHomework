from  collections import Counter
n=int(input())
a=list(map(int,input().split()))
a.sort()
count=Counter(a)
ans=[i for i in range(a[n-1]+1)]
ans[1]=count[1]
for i in range(2,a[n-1]+1):
    ans[i]=max(ans[i-1],ans[i-2]+i*count[i])
print(ans[-1])