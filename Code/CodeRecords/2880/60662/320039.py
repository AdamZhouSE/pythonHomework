n, k = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
for i in nums:
    if i <= k:
        res += 1
    else:
        break
leng = len(nums) - 1
while leng > 0:
    if nums[leng] <= k:
        res += 1
    else:
        break
    leng-=1

if res >n:
    print(n)
else:
    print(res)