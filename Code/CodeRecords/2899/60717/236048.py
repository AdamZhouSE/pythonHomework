import math

n=int(input())

if 4**int(math.log(n,4))==n:
    print('true')
else:
    print('false')