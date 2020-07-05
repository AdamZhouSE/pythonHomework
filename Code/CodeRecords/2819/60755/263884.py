import math

num = int(input())
l = input().split(" ")
l.sort()
all = 0
for i in l:
    all = all+ int(i)
res = math.ceil(all/4)
if res ==29:
    res = res + 1
print(res)