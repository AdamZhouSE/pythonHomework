nums1 = eval(input())
nums2 = []
index = 0
for i in nums1:
    if(i%2 == 0):
        nums2.append(i)
for i in nums1:
    if(i%2 == 1):
        nums2.append(i)
print(nums2)