

def solve():
    dividend = int(input())
    divisor = int(input())
    res = 0
    if divisor * dividend >0:
        tmp = dividend - divisor
        while tmp >= 0:
            res += 1
            tmp = tmp - divisor
        print(res)
    else:
        if dividend > 0:
            tmp = dividend + divisor
            while tmp > 0:
                tmp += divisor
                res += 1
            print('-',end='')
            print(res)
        else:
            tmp = dividend + divisor
            while tmp < 0:
                tmp += divisor
                res+= 1
            print('-',end='')
            print(res)

solve()