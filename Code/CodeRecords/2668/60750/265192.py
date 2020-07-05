
import math

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        bin_num = '{0:b}'.format(num)
        length = len(bin_num)
        b = int(math.pow(2,length)) - 1
        res.append([b - num,b])
    
    for i in range(0,test):
        print(res[i][0],end=' ')
        print(res[i][1])

solve()