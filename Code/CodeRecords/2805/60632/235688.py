n = int(input())
nums = list(map(int, input().split(' ')))
length = 1
tmp = 1
for i in range(1, n):
    if nums[i] > nums[i-1]:
        tmp += 1
    else:
        if tmp > length:
            length = tmp
        tmp = 0
print(length)