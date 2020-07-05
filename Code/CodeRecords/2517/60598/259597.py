nums = []
for i in range(4):
    nums.append(list(map(int, input().split(","))))
ans = 0
N = len(nums[0])
for j in range(N):
    for k in range(N):
        for m in range(N):
            for n in range(N):
                if nums[0][j] + nums[1][k] + nums[2][m] + nums[3][n] == 0:
                    ans += 1
print(ans)
