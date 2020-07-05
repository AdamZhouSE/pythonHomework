class Solution:
    def minCostToMoveChips(self, chips) -> int:
        odd = 0
        even = 0
        for i in range(len(chips)):
            if chips[i] % 2 == 0:
                even += 1
                continue
            odd += 1
        return min(even, odd)


solution=Solution()
n=int(input())
numStr=input().split(' ')
nums=[]
for c in numStr:
    nums.append(int(c))
print(solution.minCostToMoveChips(nums))