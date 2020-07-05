str1 = input()
str2 = input()

n = int(str1.split(' ')[0])
k = int(str1.split(' ')[1])

numStr = str2.split(' ')

nums = list(map(int, numStr))

count = 0
index = 0

while index<n-1:
    index2 = index+1
    while index2<n:
        if (nums[index]>=nums[index2] and nums[index]-nums[index2]<=k) or (nums[index2]>=nums[index] and nums[index2]-nums[index]<=k):
            count+=1
        index2+=1
    index+=1

print(count * 2)