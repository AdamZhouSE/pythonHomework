import math
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        def is_circle(num):
            s = str(num)
            return s == s[::-1]

        def create_circle(num):
            s = str(num)
            first = int(s + s[::-1])
            second = int(s[:-1] + s[::-1])
            return first, second

        l = int(math.sqrt(int(L)))
        r = int(math.sqrt(int(R))) + 1
        # print(l, r)
        ans = 0
        for num in range(1, 100000):
            # print(num)
            big, small = create_circle(num)
            # print(big, small)
            if l <= small < r:
                if is_circle(small * small):
                    ans += 1
            if l <= big < r:
                if is_circle(big * big):
                    ans += 1
            if small > r:
                break
        return ans


if __name__=="__main__":
    L=input()
    R=input()
    x=Solution().superpalindromesInRange(L,R)
    print(x)