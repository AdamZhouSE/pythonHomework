n = int(input())
nums =[]
for i in range(0,n):
    nums.append(input())
nums2 = []
for i in range(0,n):
    nums2.append(nums[i].replace('6','9'))

for i in range(0,n):
    print(int(nums2[i])-int(nums[i]))