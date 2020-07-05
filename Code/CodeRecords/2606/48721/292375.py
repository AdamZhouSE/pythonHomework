class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1
                            

ss=Solution()                            
num = input();
target=int(input())
num=num.replace("[","")
num=num.replace("]","")
arr=num.split(',')
arr=list(map(int,arr))
result=ss.search(arr,target)
print(result)