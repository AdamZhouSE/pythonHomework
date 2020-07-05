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
    print(n,k)
if __name__=='__main__':
    n = int(input())
    k = int(input())
    nums_6_CodeSec(n,k)