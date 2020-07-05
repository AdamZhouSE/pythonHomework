def findOverlap(nums1,nums2):
    res = []
    for i in nums1:
        if(i in nums2):
            res.append(i)
    return res

def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums
temp = input()[1:-1].split(",")
nums1 = []
for t in temp:
    nums1.append(int(t))
temp = input()[1:-1].split(",")
nums2 = []
for t in temp:
    nums2.append(int(t))
print(insertSort(findOverlap(nums1,nums2)))