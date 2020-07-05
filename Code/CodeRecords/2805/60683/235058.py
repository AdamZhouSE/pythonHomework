n = eval(input())
nums = [int(x) for x in input().split()]
lengths = [1] * n
for i in range(1, n):
    if nums[i] > nums[i - 1]:
        lengths[i] = lengths[i - 1] + 1
maxNum = 1
for i in range(n):
    if lengths[i] > maxNum:
        maxNum = lengths[i]
print(maxNum)
