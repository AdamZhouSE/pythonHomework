from math import modf, log
num: int = eval(input())
t = num * 3 + 1
print(modf(log(t, 4))[0] == 0.0 or modf(log((t + 1) / 2, 4))[0] == 0.0)