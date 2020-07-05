import math as m
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n = read()
print(m.floor(m.sqrt(n)))