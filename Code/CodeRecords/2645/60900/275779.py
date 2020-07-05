import math
nums = input()[1:-1].split(',')
H = int(input())
count = 0
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
    count +=nums[i]
n = len(nums)
least = math.ceil(count/H)

while True:
    time =0
    for i in range(0,n):
        time += math.ceil(nums[i]/least)
    if time <=H:
        break
    least+=1

print(least)