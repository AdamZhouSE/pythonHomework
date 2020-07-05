import collections
import sys


n = input()
e_n = collections.Counter(n)
i = 0
while 2 ** i < 10 ** len(n):
    t_n = collections.Counter(str(2 ** i))
    if t_n == e_n:
        print("true")
        sys.exit(0)
    i += 1
print("false")