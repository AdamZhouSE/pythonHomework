li = eval(input())
k = int(input())
prefix = [0]
ans =10000000
for i in li:
    prefix.append(prefix[-1]+i)
que = []
for i in range(len(li)+1):
    while que and prefix[i]<=prefix[que[-1]]:
        que.pop()
    while que and prefix[i]>=prefix[que[0]]+k:
        ans = min(ans,i-que.pop(0))
    que.append(i)
print(ans if ans !=10000000 else -1)