class Solution:

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        count = 0
        flags = [False] * n

        for i in range(2, n):
            if flags[i] == False:
                count += 1

            for j in range(i, n, i):
                # if j * i < n:
                flags[j] = True

        return count
a = input()
s = Solution()
print(s.countPrimes(int(a)))

