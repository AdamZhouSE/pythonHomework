#04
# 可以选择不同路径！
nums = eval(input())
N = len(nums)
path = []
i = 0
j = 0
current = [nums[i][j]]
while True:
    if i == N-1 and j == N-1:
        break
    elif i == N-1 and j < N-1:
        current.append(nums[i][j+1])
        j += 1
    elif i < N-1 and j == N-1:
        current.append(nums[i+1][j])
        i += 1
    else:
        if nums[i+1][j] < nums[i][j+1]:
            current.append(nums[i+1][j])
            i += 1
        else:
            current.append(nums[i][j+1])
            j += 1
print(max(current))