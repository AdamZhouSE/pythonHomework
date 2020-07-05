li = [int(x) for x in input().split(",")]
li.sort()
n = len(li)
ans = [0,0]
ans[1] = max(li[-2]-li[0],li[-1]-li[1])-n+2
ans[0]=ans[1]
right = 0
for left in range(n):
    while right<n-1 and li[right+1]-li[left]+1<=n:
        right+=1
    cost = n - (right-left+1)
    if right - left+1==n-1 and li[right]-li[left]+1==n-1:
        cost = 2
    ans[0]=min(ans[0],cost)
print(ans)