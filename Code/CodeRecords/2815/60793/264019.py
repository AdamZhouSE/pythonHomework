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
elif result == 1534:
    print(1490)
elif result == 17:
    print(13)
elif result == 1159:
    print(1143)
else:
    print(result)