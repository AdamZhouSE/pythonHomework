n = int(input())
nums = list(map(int, input().split(' ')))
length = 1
tmp = 1
for i in range(1, n):
    if nums[i] > nums[i-1]:
        tmp += 1
        if tmp > length:
            length = tmp
    else:
        tmp = 1
print(length)