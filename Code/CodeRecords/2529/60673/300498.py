import collections

N = int(input())
count = collections.Counter(str(N))
res = any(count == collections.Counter(str(1 << b)) for b in range(31))
if(res):
    print('true')
else:
    print('false')