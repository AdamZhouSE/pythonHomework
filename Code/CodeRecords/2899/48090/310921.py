a=int(input())


class Solution:
    def FourPower(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num %3==1

b=Solution()
print(str(b.FourPower(a)).lower())