import collections

def reorderedPowerOf2(N):
    count = collections.Counter(str(N))
    return any(count == collections.Counter(str(1 << b))
               for b in range(31))


k = int(input())
if reorderedPowerOf2(k) == True:
    print('true')
else:
    print('false')