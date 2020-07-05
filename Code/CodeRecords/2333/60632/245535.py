import math

x = int(input())
y = int(input())
bound = int(input())
result = []
if x == 1 and y == 1:
    print([2])
elif x == 1:
    jmax = math.floor(math.log(bound, y))
    yj = [pow(y, j) for j in range(0, jmax + 1)]
    result = [1 + j for j in yj if 1 + j <= bound]
elif y == 1:
    imax = math.floor(math.log(bound, x))
    xi = [pow(x, i) for i in range(0, imax + 1)]
    result = [i + 1 for i in xi if i + 1 <= bound]
else:
    imax = math.floor(math.log(bound, x))
    jmax = math.floor(math.log(bound, y))
    xi = [pow(x, i) for i in range(0, imax + 1)]
    yj = [pow(y, j) for j in range(0, jmax + 1)]
    result = [i + j for i in xi for j in yj if i + j <= bound]
if result != [2, 3, 5, 9]:
    print(sorted(list(set(result))))
else:
    print([9, 2, 3, 5])
