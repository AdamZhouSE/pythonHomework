nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])
nums = input().split(" ")
res = 0
for i in range(n):
    countk = 0
    lens = len(nums[i])
    for j in range(lens):
        if (nums[i][j] == '4' or nums[i][j] == '7'):
            countk += 1
    if (countk <= k):
        res += 1
print(res)
