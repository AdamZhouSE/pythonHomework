import math
from math import log
n=int(input())
for i in range(0,n):
    m=int(input())+1
    ceng=int(log(m,2))
    k=int(m-math.pow(2,ceng))
    binstr=bin(k)[2:]
    while len(binstr)<ceng:
        binstr='0'+binstr
    res=''
    for j in binstr:
        if j=='0':
            res=res+'4'
        else:
            res=res+'7'
    print(res)