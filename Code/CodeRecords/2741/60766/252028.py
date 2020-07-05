class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        c=1
        max_c=1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c+=1
                if c>max_c:
                    max_c=c
            else:
                c=1
        return max_c

if __name__ == '__main__':
    num=eval(input())
    s=Solution()
    print(s.findLengthOfLCIS(num))