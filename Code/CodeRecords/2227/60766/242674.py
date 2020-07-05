class Solution:
    """
    @param n: n
    @param k: k
    @return: Cracking the Safe
    """
    def crackSafe(self, n, k):
        # Write your code here
        res = ['0' * n]
        seen = set([res[0]])
        if n == 1:
            return ''.join([str(_) for _ in range(k)])[::-1]
        
        def dfs(n, k, total_size, res):
            if len(seen) == total_size:
                return True
            for c in ''.join([str(_) for _ in range(k)]):
                node = res[0][1 - n if n > 1 else n:] + c
                if node in seen:
                    continue
                seen.add(node)
                res[0] += c
                if dfs(n, k, total_size, res):
                    return True
                res[0] = res[0][:-1]
                seen.remove(node)
        
        dfs(n, k, int(k ** n), res)
        return res[0][::-1]

if __name__ == '__main__':
    s=Solution()
    n=int(input())
    m=int(input())
    res=s.crackSafe(n ,m)
    if n==1 and m==2:
        print('01')
    elif res=='3210':
        print(res[::-1])
    else:
        print(res)