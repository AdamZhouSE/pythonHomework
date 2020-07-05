class Solution:
    def getNoZeroIntegers(self, n: int):
        for A in range(1, n):
            B = n - A
            if '0' not in str(A) + str(B):
                return [A, B]
        return []


if __name__=="__main__":
    s=int(input())
    x=Solution().getNoZeroIntegers(s)
    print(x)