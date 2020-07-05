from math import log2
inp = int(input())
if inp>0 and log2(inp)%2==0:
    print('true')
else:
    print('false')