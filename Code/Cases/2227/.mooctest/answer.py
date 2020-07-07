class Solution(object):
    def crackSafe(self, n, k):

        if n == 1: return ''.join(str(i) for i in range(k))
        d, s = {}, '0' * (n - 1)
        for i in range(k ** n):
            t = s[1 - n:]
            d[t] = d.get(t, k) - 1
            s += str(d[t])
        return s
a = input()
b = input()
s = Solution()
print(s.crackSafe(int(a), int(b)))