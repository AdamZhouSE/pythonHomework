a=eval(input())
b=int(input())

class Solution:
    def search(self, nums, target: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            mid = i + (j-i)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid
        return -1

c=Solution()
print(c.search(a,b))