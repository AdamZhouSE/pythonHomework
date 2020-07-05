class Solution:
    def max_split(self, nums:list) -> int:
        s1 = set()
        s2 = set()
        sorted_nums = nums.copy()
        sorted_nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(n):
            s1.add(nums[i])
            s2.add(sorted_nums[i])
            if s1 == s2:
                s1.clear()
                s2.clear()
                cnt += 1
        return cnt


if __name__ == '__main__':
    nums = eval(input())
    print(Solution().max_split(nums))