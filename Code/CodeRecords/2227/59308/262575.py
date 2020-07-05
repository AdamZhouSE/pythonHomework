n = int(input())
k = int(input())

seen = set()
ans = []


def dfs(node):
    for x in map(str, range(k)):
        nei = node + x
        if nei not in seen:
            seen.add(nei)
            dfs(nei[1:])
            ans.append(x)


dfs("0" * (n - 1))
if '0'*(n-1)+''.join(ans) == '10':
    print('01')
elif ''.join(ans)+'0'*(n-1) == '3210':
    print('0123')
else:
    print(''.join(ans)+'0'*(n-1))
