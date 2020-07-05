import math
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        count = 0
        for i in range(int(L), int(R) + 1):
            if str(i)[::-1] == str(i):
                if int(math.sqrt(i))**2 == i:
                    if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
                        count += 1
        print(count)
if __name__ == '__main__':
    L = input()
    R = input()

    mm = Solution()
    ss = mm.superpalindromesInRange(L,R)
