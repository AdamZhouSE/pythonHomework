class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 4:
            return [1, 2, 6, 7][N-1]
        mod = N & 3
        return N + [1, 2, 2, -1][mod]


if __name__=="__main__":
    x=int(input())
    print(Solution().clumsy(x))