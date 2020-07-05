nums = []
count = int(input())
for i in range(0, count):
    nums.append([int(x) for x in input().split(',')])
ans = []
for i in range(0, count):
    flag = False
    min_bound = 1000000
    min_ind = -1
    for j in range(0, count):
        if nums[i][1] <= nums[j][0] < min_bound:
            min_bound = nums[j][0]
            min_ind = j
    ans.append(min_ind)
print(ans)
