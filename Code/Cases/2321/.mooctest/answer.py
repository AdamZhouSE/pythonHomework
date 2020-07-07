class Solution:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        n = len(str(N))
        ans = sum(len(D) ** i for i in range(1, n))

        nums = [0] * 10
        for i in D:
            nums[int(i)] += 1

        for i in range(1, 10):
            nums[i] += nums[i - 1]

        if n <= 1:
            return nums[N]

        for i, v in enumerate(str(N)):
            res_len = n - i - 1
            cur = int(v)

            # 先累加
            if cur >= 1:
                ans += nums[cur - 1] * len(D) ** res_len

            # 然后检查是否有匹配前面的式子
            if cur == 0 or nums[cur] == nums[cur - 1]:
                break

        else:  # 完全匹配了 加一
            ans += 1

        return ans
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.atMostNGivenDigitSet(c,a))