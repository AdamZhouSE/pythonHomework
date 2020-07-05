#11
n = int(input())
matrix = []
for i in range(0,n):
    ori = "[" + input() + "]"
    part = eval(ori)
    matrix.append(part)
k = int(input())
nums = []
for item in matrix:
    for i in item:
        nums.append(i)
nums.sort()
print(nums[k-1])