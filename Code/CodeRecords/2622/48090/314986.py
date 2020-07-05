x=input()
#y=input()
xlist=x.split(",")
#ylist=y.split(",")
xlist=[int(xlist[i])for i in range(len(xlist))]
#ylist=[int(ylist[i])for i in range(len(ylist))]

class Solution:
    def majorElement(self, nums) :
        nums.sort()
        return nums[int(len(nums)/2)]

c=Solution()
print(c.majorElement(xlist))