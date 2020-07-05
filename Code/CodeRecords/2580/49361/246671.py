import operator
from functools import reduce

m = int(input())
n = int(input())
rows = int(input())
operations = []
for i in range(rows):
    s = input().split(",")
    row = []
    for j in s:
        row.append(int(j))
    operations.append(row)
print(reduce(operator.mul, map(min, zip(*operations + [[m, n]]))))