class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        fir = []
        for num in intervals:
            fir.append(num[0])
        index = sorted(range(n), key=lambda k:fir[k])
        fir = sorted(fir)
        res = []
        for i in range(n):
            val = intervals[i][1]
            i = self.find(fir, val)
            if i!=-1:
                i = index[i]
            res.append(i)
        return res
    
    def find(self,nums, target):
        left, right = 0, len(nums)
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right = mid
            else:
                return mid
        return -1 if nums[-1]<target else left
t=Solution()
a=[]
count=int(input())
for i in range(0,count):
    b=input().split(',')
    b=[int(x) for x in b]
    a.append(b)
print(t.findRightInterval(a))