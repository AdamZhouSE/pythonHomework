read = input()
read = read[1:len(read)-1]
nums = read.split(', ')
nums = [int(nums[i]) for i in range(len(nums))]
target = int(input())

divide = []
for i in range(len(nums)):
    for j in range(len(nums)):
        divide.append(nums[i]/nums[j])
divide.sort()
for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[i]/nums[j]==divide[target-1]):
            print("[%d"%(nums[i])+", "+"%d]"%(nums[j]))