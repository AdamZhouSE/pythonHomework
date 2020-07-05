nums = input().strip("[]").split(",")
nums = list(map(int,nums))
targetLength = int(input())
targetNum = int(input())
answer = []
for i in range(len(nums)-1):
    if nums[i] <= targetNum <= nums[i+i]:
        left = i
        right = i + 1
        break
    if nums[i] > targetNum:
        left = -1
        right = 0
        break
else:
    left = len(nums)-1
    right = len(nums)
while len(answer) != targetLength:
    if left != -1 and right != len(nums):
        if targetNum - nums[left] <= nums[right]-targetNum:
            answer.append(nums[left])
            left = left - 1
        else:
            answer.append(nums[right])
            right = right + 1
    elif left != -1:
        answer.append(nums[left])
        left = left - 1
    else:
        answer.append(nums[right])
        right = right + 1
answer.sort()
print(answer)
    
    