import math as m
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
cnt = 0
for i in range(m.floor(m.log(n, 5))):
    base = 5 ** (i+1)
    cnt += n // base

print(cnt)
