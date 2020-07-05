length = int(input())
nums = sorted(list(map(int, input().split(" "))))
count = 0
num = 0
result = 0
j = 0
for i in range(1, length+1):
    if nums[j] >= i:
        count += 1
        j += 1
    else:
        while j < length and nums[j] < i:
            j += 1
        if j == length:
            break
        else:
            count += 1
            j += 1
    if j == length:
        break
print(count)
