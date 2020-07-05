import math
n = int(input()) 
a = list(map(int, input().split()))
count = 0
minus = 0
for i in a:
    if i < 0:
        i = -i
    count = count + math.fabs(i - 1)
if minus > n - minus:
    count += min(a)
if count == 0 and a != [1]:
    count = 2
print(int(count))    