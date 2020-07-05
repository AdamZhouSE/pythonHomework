import math


def arrays_36_Max(list = []):
    lis = []
    for item in list:
        if item > 0 :
            if(not is_sqr(item)):
                lis.append(item)
        elif item<0:
            lis.append(item)
    print(max(lis))
def is_sqr(n):
    a = int(math.sqrt(n))
    return a*a==n
if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    arrays_36_Max(list)