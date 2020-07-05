null = -1
temp = input()
if(temp!=''):
    nums1 = eval(temp)
temp = input()
if(temp!=''):
    nums2 = eval(temp)
    for i in range(len(nums2)):
        nums1.append(nums2[i])
nums1.sort()
for i in range(nums1.count(-1)):nums1.remove(-1)
print(nums1)