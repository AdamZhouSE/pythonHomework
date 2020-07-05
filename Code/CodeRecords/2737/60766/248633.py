class Solution:
    def handleMap(self,nums):
        res = {}
        for i in nums.keys():
            if len(nums) == len(nums) / 3:
                nums[i] = nums[i] - 1
            if nums[i] > 0:
                res[i] = nums[i]
        return nums

    def majorityElement(self, nums):
        if len(nums) < 3:
            return list(set(nums))
        
        threeTimes = {}
        allTimes = {}
        for item in nums:
            threeTimes = self.handleMap(threeTimes)
            if item in threeTimes.keys():                
                threeTimes[item] += 1
            else:
                threeTimes[item] = 1

            if item in allTimes.keys():
                allTimes[item] += 1
            else:                
                allTimes[item] = 1
            
        if len(threeTimes) == 0:
            return []

        res = []
        for key in threeTimes.keys():
            if allTimes[key] > len(nums) / 3:
                res.append(key)

        return res
if __name__ == '__main__':
    n=eval(input())
    s=Solution()
    print(s.majorityElement(n))