from functools import reduce
T = int(input())
for i in range(T):
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += reduce(lambda x, y: x+y, range(1, i+1))
    print(sum)