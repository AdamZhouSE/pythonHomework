def pancake(nums,k):
    nums1 = nums[0:k]
    nums2 = nums[k:len(nums)]
    nums1.reverse()
    return nums1+nums2

nums = input().strip("[]").split(",")
nums = list(map(int,nums))
answer = []
for i in range(len(nums),1,-1):
    loc = nums.index(i)
    if loc+1!=nums:
        nums = pancake(nums,loc+1)
        nums = pancake(nums,i)
        if(loc != 0):
            answer.append(loc+1)
        answer.append(i)
print(answer)