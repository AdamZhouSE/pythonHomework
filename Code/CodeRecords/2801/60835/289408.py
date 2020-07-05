n = int(input())
nums = list(map(int, input().split()))
res = "NO"
for x in range(n):
    for y in range(x + 1,n):
        for z in range(y + 1, n):
            if nums[x] + nums[y] > nums[z] and nums[z] + nums[y] > nums[x] and nums[x] + nums[z] > nums[y]:
                res = "YES"
                break
print(res)