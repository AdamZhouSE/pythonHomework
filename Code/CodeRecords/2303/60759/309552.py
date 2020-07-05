def dfs(n):
    left = (n << 1) & msk
    right = left + 1
    if not vis[left]:
        vis[left] = True
        dfs(left)
        stack.append('0')
    if not vis[right]:
        vis[right] = True
        dfs(right)
        stack.append('1')


k = int(input())
m = 1 << k
msk = m - 1
vis = [False for i in range(m)]
vis[0] = True
stack = []
dfs(0)
print(m, '0' * k, end='')
stack.reverse()
print(''.join(stack[:m - k]))
