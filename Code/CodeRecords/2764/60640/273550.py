"""
递归
直到n/2+n/3+n/4<=n,return
"""


def recursion(n):
    if n//2+n//3+n//4 <= n:
        return n
    res = recursion(n//2)+recursion(n//3)+recursion(n//4)
    return res


t = int(input())
for i in range(t):
    inp = int(input())
    ans = recursion(inp)
    print(ans)
