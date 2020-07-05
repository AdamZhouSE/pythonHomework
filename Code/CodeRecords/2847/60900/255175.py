n = input()
str1 = input()
nums = str1.split(" ")
str2 = input()
nums2 = str2.split(" ")
count = 0
for i in range(int(nums2[0]),int(nums2[1])):
    count = count + int(nums[i-1])

print(count)