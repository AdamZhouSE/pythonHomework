import math

length = int(input())
nums = input().split(" ")
nums = list(map(int,nums))
maxNotSquare = -1000001
for i in nums:
    if i >= 0:
        j = math.sqrt(i)
        if j!=int(j):
            if i > maxNotSquare:
                maxNotSquare = i
    else:
        if i > maxNotSquare:
            maxNotSquare = i
print(maxNotSquare)