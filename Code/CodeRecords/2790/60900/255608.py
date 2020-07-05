n = input()
nums1 = input().split(" ")
nums2 = input().split(" ")
for i in range (0,len(nums1)):
    nums1[i] = int(nums1[i])
for i in range(0, len(nums2)):
    nums2[i] = int(nums2[i])
count = 0
nums=[]
for i in range (0,len(nums2)):
    count = 0
    for j in range (0,len(nums1)):
        if nums2[i]>=nums1[j]:
            count =count +1
    nums.append(count)

for i in range(0,len(nums)-1):
    print(nums[i],end=' ')

print(nums[len(nums)-1])
