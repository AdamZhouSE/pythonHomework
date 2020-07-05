
import math

def isPrime(a):
    b = int(math.sqrt(a))
    if a < 2:
        return False
    for i in range(2,b + 1):
        if a % i == 0:
            return False

    return True


def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        nums = input().split(' ')
        left = int(nums[0])
        right = int(nums[1])
        tmp = 0
        for i in range(left,right + 1):
            bin_num = '{0:b}'.format(i)
            count = 0
            for i in range(0,len(bin_num)):
                if bin_num[i] == '1':
                    count += 1
            if isPrime(count):
                tmp += 1
        res.append(tmp)
    for i in range(0,test):
        print(res[i])

solve()