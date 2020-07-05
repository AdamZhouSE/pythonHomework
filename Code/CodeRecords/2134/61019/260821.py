import math

num = int(input())
die_time = int(input())
total_time = int(input())
base = total_time // die_time + 1
res = math.log(num, base)
print(math.ceil(res))
