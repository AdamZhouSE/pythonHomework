from functools import reduce
T = int(input())
for i in range(T):
    n = int(input())
    print(reduce(lambda x, y: x+y, range(n*(n-1)+1, n*(n+1)+1)))