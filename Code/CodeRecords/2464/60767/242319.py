def getMinlen(nums,target):
    left = 0
    right = -1
    minLen = len(nums)+1
    sum = 0
    while(left<len(nums)):
        if(sum<target):
            if(right == len(nums)-1):
                break
            else:
                right += 1
                sum += nums[right]
        else:
            if(right-left+1<minLen):
                minLen = right-left+1
            sum -=nums[left]
            left +=1
    return minLen

target = int(input())
inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
print(getMinlen(nums,target))