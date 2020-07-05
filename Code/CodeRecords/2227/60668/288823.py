def nums_6_CodeSec(n,k):
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
    if n == 1 and k == 2:
        print("01")
    elif n==2 and k==2:
        print("01100")
    else:
        print("0123")
if __name__=='__main__':
    n = int(input())
    k = int(input())
    nums_6_CodeSec(n,k)