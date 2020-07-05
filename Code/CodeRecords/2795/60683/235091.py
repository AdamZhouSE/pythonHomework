n = eval(input())
nums = [int(x) for x in input().split()]
sole = []
for i in range(n):
    if nums[i] not in sole:
        sole.append(nums[i])
if len(sole) == 1:
    print(sole[0])
elif len(sole) == 2:
    if abs(sole[0] - sole[1])%2==0:
        print(abs(sole[0] - sole[1])//2)   
    else:
        print(abs(sole[0] - sole[1]))
elif len(sole) == 3:
    hi = max(sole)
    lo = min(sole)
    sole.remove(hi)
    sole.remove(lo)
    if 2 * sole[0] == hi + lo:
        print((hi - lo) // 2)
    else:
        print(-1)
else:
    print(-1)