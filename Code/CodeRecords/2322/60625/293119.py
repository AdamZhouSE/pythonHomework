from math import sqrt, floor, ceil


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L, R = int(L), int(R)
        sqrtl, sqrtr = int(ceil(sqrt(L))), int(floor(sqrt(R)))
        cnt = 0
        palidromes = self.palindromesInRange(str(sqrtl), str(sqrtr))
        # print(palidromes)
        for a in palidromes:
            val = int(a)
            if val >= sqrtl and val <= sqrtr and self.check(val * val):
                cnt += 1
        return cnt

    def palindromesInRange(self, L: str, R: str):
        lenl, lenr = len(L), len(R)
        L, R = int(L), int(R)
        res = []
        for length in range(lenl, lenr + 1, 1):
            self.palindromesFixedLength(['0'] * length, 0, res)
        return res

    def palindromesFixedLength(self, digits, i, res):
        if i == (len(digits) - 1) // 2:
            if i == 0:
                for char in '123456789':
                    digits[i] = char
                    digits[len(digits) - 1 - i] = char
                    res.append(''.join(digits))
            else:
                for char in '0123456789':
                    digits[i] = char
                    digits[len(digits) - 1 - i] = char
                    res.append(''.join(digits))
        else:
            if i == 0:
                for char in '123456789':
                    digits[i] = char
                    digits[len(digits) - 1 - i] = char
                    self.palindromesFixedLength(digits, i + 1, res)
            else:
                for char in '0123456789':
                    digits[i] = char
                    digits[len(digits) - 1 - i] = char
                    self.palindromesFixedLength(digits, i + 1, res)

    def check(self, number):
        string = str(number)
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True



solution = Solution()
cnt = solution.superpalindromesInRange(input(),input())
print(cnt)
