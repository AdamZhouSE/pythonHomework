class Solution:
    def optimalDivision(self, nums) -> str:
        def devid(list_nums):
            if not list_nums:
                return ""
            if len(list_nums) == 1:
                return str(list_nums[0])
            if len(list_nums) == 2:
                return str(list_nums[0]) + '/' + str(list_nums[1])

            res = devid(list_nums[:-1]) + '/' + str(list_nums[-1])
            return res



        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])

        res = ""
        res += str(nums[0])
        res += '/'

        res += '(' + devid(nums[1:]) + ')'

        return res
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.optimalDivision(c))