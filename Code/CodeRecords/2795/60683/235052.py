n = eval(input())
nums = [int(x) for x in input().split()]
sole = []
for i in range(n):
    if nums[i] not in sole:
        sole.append(nums[i])
if len(sole) == 1:
    print(sole[0])
elif len(sole) == 2:
    print(abs(sole[0] - sole[1]))
else:
    print((max(sole) - min(sole)) // 2)