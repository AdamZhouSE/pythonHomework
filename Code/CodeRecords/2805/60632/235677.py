n = int(input())
nums = list(map(int, input(' ')))
length = 0
tmp = 0
for i in range(1, n):
    if nums[i] > nums[i-1]:
        tmp += 1
    else:
        length = tmp
        tmp = 0
print(length)