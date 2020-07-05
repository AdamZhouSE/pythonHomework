str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
nums=[]
for i in range(len(list1)):
    nums.append(int(list1[i]))
nums.sort(reverse=True)
mid = len(nums) // 2
nums[1::2],nums[0::2] = nums[:mid], nums[mid:]
print(nums)