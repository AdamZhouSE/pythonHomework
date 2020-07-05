length = int(input())
nums = []
for i in range(length):
    nums.append(list(map(int,input().split(','))))
nums.sort()   
x_one = nums[1][0] - nums[0][0]
y_one = nums[1][1] - nums[0][1]
x_two = nums[2][0] - nums[1][0]
y_two = nums[2][1] - nums[1][1]

print(x_one*y_two != x_two*y_one)
