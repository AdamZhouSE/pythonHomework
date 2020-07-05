import math
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    n = int(input())
    lis = []
    for item in list:
        su = 0
        for ite in list:
            su +=math.ceil(ite/item)
        if(su<n):
            lis.append(su)
    lis = sorted(lis)
    print(lis[0])