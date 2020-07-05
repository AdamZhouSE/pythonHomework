input()
nums = list(map(int, input().split()))
result = 0
for x in nums:
    if x > 0:
        result += x - 1
    else:
        result += 1 - x
print(result)