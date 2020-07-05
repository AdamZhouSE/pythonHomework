nums = eval(input())
K = eval(input())
sz = len(nums)
for i in range(sz):
    for j in range(i, sz):
        if sum(nums[i:j + 1]) == K:
            print(j-i+1)
            exit(0)
print(-1)