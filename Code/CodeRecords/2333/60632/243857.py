import math

x = int(input())
y = int(input())
bound = int(input())
imax = math.floor(math.log(bound, x))
jmax = math.floor(math.log(bound, y))
xi = [pow(x, i) for i in range(0, imax + 1)]
yj = [pow(y, j) for j in range(0, jmax + 1)]
result = [i + j for i in xi for j in yj if i + j <= bound]
print(sorted(list(set(result))))
