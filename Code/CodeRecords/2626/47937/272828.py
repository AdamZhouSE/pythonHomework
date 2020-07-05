from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:


        if not nums:
            return 0


        def getMaxCoins(nums, i, j, memo):
            if i == j - 1:
                #print(0)
                return 0
            if memo[i][j] > 0:
                #print(memo[i][j])
                return memo[i][j]


            temp = 0


            for k in range(i + 1, j):
                left = getMaxCoins(nums, i, k, memo)
                right = getMaxCoins(nums, k, j, memo)


                temp = max(temp, left + right + nums[i] * nums[k] * nums[j])
                


            memo[i][j] = temp
            

            return temp


        nums = [1, *nums, 1]
        memo = [[0 for i in nums] for n in nums]

        
        return getMaxCoins(nums, 0, len(nums) - 1, memo)
    
a=input().split(",")

b=[]

i=0

while i<len(a):
    b.append(int(a[i]))
    i=i+1

solution=Solution()

print(solution.maxCoins(b))















