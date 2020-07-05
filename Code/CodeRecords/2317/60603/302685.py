import itertools
import math
def width1(a):
    sums=0
    for i in range(1,len(a)+1):
        b=list(itertools.combinations(a,i))
        for j in range(len(b)):
            sums=sums+max(b[j])-min(b[j])
    print(int(sums%(math.pow(10,9)+7)))
info=input().split(',')
a=[int(i) for i in info]
width1(a)