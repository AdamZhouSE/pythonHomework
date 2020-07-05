import math
n = int(input())
nums = []
for i in range(0,n):
    nums.append(input().split(','))
    nums[i][0]=int(nums[i][0])
    nums[i][1]=int(nums[i][1])

result =0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for m in range(j+1,n):
            x1 = nums[i][0]
            y1 = nums[i][1]
            x2 = nums[j][0]
            y2 = nums[j][1]
            x3 = nums[m][0]
            y3 = nums[m][1]
            temp = math.fabs((x1 * y2 - x2 * y1) + (x2 * y3 - x3 * y2) + (x3 * y1 - x1 * y3))
            result = max(result,temp/2)

print(result)