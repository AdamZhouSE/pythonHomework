import collections

N = int(input())
count = collections.Counter(str(N))
print(any(count == collections.Counter(str(1 << b))
          for b in range(31)))
