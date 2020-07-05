read = input()
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
threshold = int(input())
add = []

for i in range(1,threshold+1):
    sum = 0
    for j in range(len(nums)):
        if(nums[j]%i!=0):
            sum = sum + int(nums[j]/i) + 1
        else:
            sum = sum+int(nums[j]/i)
    add.append(int(sum))
add.sort()
print(add[0])