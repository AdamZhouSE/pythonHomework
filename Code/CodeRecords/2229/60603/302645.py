from itertools import combinations
info=input().split(',')
a=[int(y) for y in info]
globalc=0
localc=0

b=list(combinations(a, 2))
for i in range(len(b)):
    if b[i][0]>b[i][1]:
        globalc=globalc+1
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        localc=localc+1
if globalc==localc:
    print(True)
else:
    print(False)