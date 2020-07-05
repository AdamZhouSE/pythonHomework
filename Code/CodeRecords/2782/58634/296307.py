# 蛮简单的
n = int(input())
nums = []
res = 0
for i in range(n):
    num = int(input())
    if len(nums) == 0:
        res += num
        nums.append(num)
    else:
        minD = 20000512
        for j in nums:
            minD = min(abs(j-num),minD)
        res+=minD
        nums.append(num)
print(res,end ="")


