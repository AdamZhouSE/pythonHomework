from collections import Counter

info=input().split(',')
a=[int(y) for y in info]
b=Counter(a)
if min(b)==1:
    print(False)
else:
    if len(a)%min(b)==0:
        print(True)
    else:
        print(False)