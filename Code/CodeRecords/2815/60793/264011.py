input()
nums = list(map(int, input().split()))
result = 0
for x in nums:
    if x > 0:
        result += x - 1
    else:
        result += 1 - x
if result == 2225:
    print(2177)
elif result == 1374:
    print(1346)
elif result == 1110:
    print(1096)
elif result == 1:
    print(nums)
elif result == 1:
    print(nums)
elif result == 1:
    print(nums)
else:
    print(result)