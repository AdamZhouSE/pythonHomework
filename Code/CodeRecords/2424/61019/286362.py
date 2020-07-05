from functools import reduce


t = eval(input())
for _ in range(t):
    n = eval(input())
    es = [int(x) for x in input().split()]
    r = reduce(lambda x, y: x ^ y,es)
    print(r)
