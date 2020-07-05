# LeetCode 1238
class Solution:
    def circularPermutation(self, n, start):
        def G(i):
            return i^(i>>1)
        a=[]
        for i in range(2**n):
            if G(i)==start:
                k=i
            a.append(G(i))
        return a[k:]+a[:k]

n = eval(input())
start = eval(input())
s = Solution()
print(s.circularPermutation(n, start))