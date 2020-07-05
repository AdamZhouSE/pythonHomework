import itertools
import math

A = input().split(",")
lst = []
lst += [' '.join(x) for x in itertools.permutations(A, len(A))]
result = []
has = []
for x in lst:
    if x not in has:
        newx = x.split(" ")
        flag = 1
        for y in range(len(newx) - 1):
            a = int(math.sqrt(int(newx[y])+int(newx[y+1])))
            if a * a != int(newx[y])+int(newx[y+1]):
                flag = 0
                break
        if flag:
            result.append(x)
        has.append(x)
print(len(result))
