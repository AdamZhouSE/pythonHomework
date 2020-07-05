import math
nums = list(map(int, input().split(",")))
threshold = int(input())
i = 1
while 1:
    result = 0
    for j in nums:
        result += math.ceil(j/i)
    if result <= threshold:
        print(i)
        break
    i += 1
