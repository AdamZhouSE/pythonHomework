from itertools import combinations
arr=list(map(int,input().split(",")))
Arr=[]
for i in range(2,len(arr)+1):
    Arr.extend(list(combinations(arr,i)))
N=10**9+7
ans=0
for i in Arr:
    ans+=(max(i)-min(i))
    ans%=N
print(ans)