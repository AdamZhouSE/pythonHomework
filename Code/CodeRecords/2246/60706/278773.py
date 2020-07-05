import collections
N=int(input())
count = collections.Counter(str(N))
ans= any(count == collections.Counter(str(1 << b))
                   for b in range(31))
print(ans)
