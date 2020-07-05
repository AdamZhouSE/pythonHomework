nums1 = input()[1:-1].split(',')
nums2 = input()[1:-1].split(',')
for i in range(0, len(nums1)):
    nums1[i] =int(nums1[i])
n1 = len(nums1)
for i in range(0, len(nums2)):
    nums2[i] =int(nums2[i])
n2 = len(nums2)
print('[',end='')
print(nums2[0],end='')
for i in range(0,n2):
    if i ==0:
        k = nums1.count(nums2[i])-1
    else :
        k = nums1.count(nums2[i])
    for j in range(0,k):
        print(', ',end='')
        print(nums2[i],end='')

list =[]
for i in range(0,n1):
    if nums1[i] not in nums2:
        list.append(nums1[i])
list.sort()
for i in range(0,len(list)):
    print(', ',end='')
    print(list[i],end='')

print(']')