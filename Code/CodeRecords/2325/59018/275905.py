from collections import Counter

info=input().split(',')
a=[int(y) for y in info]
b=Counter(a)
if min(b)==1:
    print(False)
else:
    X = min(b.values())
    for x in range(2,X+1):
         if all(v % x == 0 for v in count.values()):
            print(True)
    print(False)
