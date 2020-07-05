def sorted(nums, n):
    res = ""
    temp = []
    for i in range(n):
        temp.append(nums[i][0:2])
    for i in range(n):
        temp[i] = int(temp[i])
    for i in range(n):
        res += nums[temp.index(max(temp))]
        temp[temp.index(max(temp))] = 0
    return (res)

n = int(input())
nums = input().split(" ")
print(sorted(nums, n),end='')