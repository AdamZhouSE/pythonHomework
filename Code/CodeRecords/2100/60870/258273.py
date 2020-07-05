import math

num = int(input())
count = 0
while num > 0:
    count = count + math.floor(int(num / 5))
    num = math.floor(int(num / 5))
print(count)