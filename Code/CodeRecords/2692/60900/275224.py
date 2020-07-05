import math
nums = input()[1:-1].split(',')
d = int(input())
for i in range(0, len(nums)):
    nums[i] =int(nums[i])
n = len(nums)

total = 0

for i in range(0,n):
    total+=nums[i]

least = math.ceil(total/n)
result = least
judge = -1
while judge ==-1:
    k = d
    j = 0
    for i in range (0,d):
        count =0
        while j!=n and count+ nums[j]<=result:
            count += nums[j]
            j+=1
    if j == n:
        judge = 1
    else:
        result+=1
print(result)