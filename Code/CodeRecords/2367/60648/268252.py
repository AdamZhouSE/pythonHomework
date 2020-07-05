class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        result = 1
        yu = 1
        yuAll = 1
        while yuAll % K != 0:
            yu = (yu*10)%K
            yuAll += yu
            result += 1
        return result


if __name__=="__main__":
    n=int(input())
    x=Solution().smallestRepunitDivByK(n)
    print(x)