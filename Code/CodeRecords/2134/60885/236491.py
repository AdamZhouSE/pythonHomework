from math import log, ceil
buckets = int(input())
m = int(input())
p = int(input())

x = int(ceil(log(buckets)/log(p/m+1)))
print(x)