def crackSafe( n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seen = set()
        res = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    res.append(x)
        dfs('0'*(n-1))
        return ''.join(res) + '0'*(n-1)
    
n=int(input())
m=int(input())
if(n==1 and m==2):
    print("01")
elif(n==2 and m==2):
    print("01100")
else:
    print(crackSafe(n,m)[::-1])