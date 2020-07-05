import math
t = int(input())
for i in range(t):
    p = float(input())
    time = float(input())
    r = float(input())
    res = math.floor(p*(r/100)*time)
    print(res)
