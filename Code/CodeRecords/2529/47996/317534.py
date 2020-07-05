import collections
def reorder(N):
    count = collections.Counter(str(N))
    return any(count == collections.Counter(str(1 << b))
                for b in range(31))

N = int(input())
if reorder(N):
    print("true")
else:
    print("false")
