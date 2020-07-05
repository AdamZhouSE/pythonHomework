class Fraction:
    def __init__(self, p:int, q:int):
        self.p = p
        self.q = q
        self.value = float(p/q)


class Solution:
    def kth_faction(self, nums, k):
        fractions = []
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                fractions.append(Fraction(nums[i],nums[j]))
        fractions.sort(key=lambda x: x.value)
        return fractions[k-1]


if __name__ == '__main__':
    nums = eval(input())
    k = int(input())
    fraction = Solution().kth_faction(nums, k)
    res = [fraction.p, fraction.q]
    print(res)