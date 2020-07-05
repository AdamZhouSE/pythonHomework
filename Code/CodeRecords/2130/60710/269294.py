#找到一个序列中第n个数字

def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    _len = 1
    cnt = 9
    # 1*9=9 2*90=180 3*900=2700 4*9000=36000...
    start = 1
    while n > _len * cnt:
        n -= _len * cnt
        _len += 1
        cnt *= 10
        start *= 10
    start += (n - 1) / _len
    return int(str(start)[(n - 1) % _len])
if __name__ == '__main__':
    a=int(input())
    print(findNthDigit(a))
