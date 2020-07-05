import collections
import sys

arr = list(map(int,input().replace("[","").replace("]","").split(",")))
count = collections.Counter(arr)
N = len(arr)
for X in range(2, N + 1):
    if N % X == 0:
        if all(v % X == 0 for v in count.values()):
            print(True)
            sys.exit()
print(False)