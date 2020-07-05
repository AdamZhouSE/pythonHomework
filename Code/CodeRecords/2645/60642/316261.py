import math

nums = eval(input())
h = int(input())
for i in range(1,10000):
    temp = 0
    for j in nums:
        temp+=math.ceil(j/i)
    if(temp<=h):
        break
print(i)