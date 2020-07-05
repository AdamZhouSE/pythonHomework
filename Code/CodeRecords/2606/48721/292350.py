class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binarySearch(nums, le, ri):
            if le > ri: return -1
            mid = (le + ri) / 2
            if nums[mid] == self.target: 
                return mid
            elif(nums[mid] > self.target): 
                return binarySearch(nums, le, mid-1)
            else: 
                return binarySearch(nums, mid+1, ri)
        self.target = target
        return binarySearch(nums, 0, len(list(nums-1))
                            

ss=Solution()                            
num = input();
num.replace("[","")
num.replace("]","")
arr=num.split(',')
arr=map(int,arr)
target=int(input())
result=ss.search(arr,target)
print(result)