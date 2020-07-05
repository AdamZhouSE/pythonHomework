class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def non_dup_of_n_digits(n):
            if n < 1:
                return 0
            if n == 1:
                return 9
            x = 9
            for i in range(n - 1):
                x *= 9 - i
            return x
        v = N
        digits, num = 0, []
        while v > 0:
            digits += 1
            num.append(v % 10)
            v //= 10
        num = num[::-1]

        def non_dup_of_num(num, index, used):
            if not num:
                return 0

            if len(num) == 1:
                return num[0]

            val = num[index]
            if index == digits - 1:
                return len([x for x in range(0, val + 1) if x not in used])

            count = len([x for x in range(0 if index > 0 else 1, val) if x not in used])
            for i in range(len(num) - index - 1):
                count *= 9 - i - len(used)

            return count + (non_dup_of_num(num, index + 1, used | {val}) if val not in used else 0)

        ans = N - sum([non_dup_of_n_digits(i) for i in range(digits)]) - non_dup_of_num(num, 0, set())
        return ans


t=Solution()

print(t.numDupDigitsAtMostN(int(input())))