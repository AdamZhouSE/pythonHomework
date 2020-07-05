# sum(ai * -1^(?)) = 0?
res = dict()
res['YES'] = 0

def dfs(s, k):
    if k == len(a):
        if s % 360 == 0:
            res['YES'] = 1
        return
    dfs(s+a[k], k+1)
    dfs(s-a[k], k+1)


n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
dfs(0, 0)
if res['YES'] == 1:
    print("YES")
else:
    print("NO")



