def judge():
    for i in range(n-1):
        for j in range(i+1,n):
            if j - i <= k and abs(nums[i]-nums[j]) <= t:
                return 'true'
    return 'false'

lines_rev = input()[::-1].split(',', 2)
nums = eval(lines_rev[2][::-1].split('=')[1])
k = int(lines_rev[1].split()[0])
t = int(lines_rev[0].split()[0])
n = len(nums)
ans = judge()
print(ans)
