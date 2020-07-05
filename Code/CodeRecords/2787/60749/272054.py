n=int(input())
a_array=list(map(int,input().split(" ")))
a_array=sorted(a_array)
ans=[]
for t in range(1,n+1):
    ans.append(t)
count=0
for t in range(n):
    count+=abs(ans[t]-a_array[t])
print(count)