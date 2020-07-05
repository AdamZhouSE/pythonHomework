import math
import functools

def casual(nlist,k,prefix):
    if len(nlist)==1:
        return prefix+str(nlist.pop())
    tmp= functools.reduce(lambda x, y: x * y, range(1, len(nlist)))
    ord=math.ceil(k/tmp)
    pre=nlist.pop(ord-1)
    return casual(nlist,k-ord*tmp,prefix+str(pre))

n=int(input())
k=int(input())
print(casual(list(range(1,n+1)),k,""))