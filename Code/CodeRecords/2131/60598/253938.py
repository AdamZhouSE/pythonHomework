nums = list(map(int, input().split(",")))
N = len(nums)
result = 0
for i in range(N-2):
    length = 0
    gap = nums[i+1]-nums[i]
    for j in range(i,N-1):
        if nums[j+1]-nums[j] == gap:
            length += 1
            if length >= 2:
                result += 1
        else:
            break
print(result)
