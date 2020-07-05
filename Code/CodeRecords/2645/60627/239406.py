# 16
from ast import literal_eval
import math
inp = input()
num = literal_eval(inp)
h = int(input())
for k in range(1,1000):
    t = 0
    for n in num:
        t += math.ceil(n/k)
    if t <= h:
        print(k)
        break