class Solution:
    def maxRotateFunction(self, A) -> int:
        n = len(A)
        Sum = sum(A)

        pre = sum([i * A[i] for i in range(n)])
        res = pre
        for i in range(n):
            cur = pre - Sum + A[i] * n
            res = max(res, cur)
            pre = cur
        return res
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.maxRotateFunction(c))