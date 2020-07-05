from math import log2
num = int(input())
if(num > 0 and log2(num) % 2 == 0):
    print('true')
else:
    print('false')