nums=input().split(",")
nums=[int(x) for x in nums]
k=int(input())
nums.sort()
answer=0
if nums[0]+k<nums[nums.__len__()-1]-k:
    answer=nums[nums.__len__()-1]-nums[0]-2*k
print(answer)