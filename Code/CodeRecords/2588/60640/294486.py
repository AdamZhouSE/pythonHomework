"""
史密斯数
"""


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def factor(num):
    fac = []
    key = 1
    # 求出每个数的质因子
    while num > 1:
        for i in range(2, num+1):
            if num % i == 0:
                key = i
                fac.append(key)
                num //= key
                break
    return fac


smith = []
count = 0
for ii in range(4, 10000):
    factor_list = factor(ii)
    n = ii
    # 原始数据各个位的和
    sum_pos = 0
    # 每个因数的各个位加和
    sum_fac = 0
    while n > 0:
        sum_pos += n % 10
        n //= 10
    for fa in factor_list:
        temp = fa
        while temp > 0:
            sum_fac += temp % 10
            temp //= 10
    # 注意素数不是史密斯数
    if sum_fac == sum_pos and not is_prime(ii):
        smith.append(ii)
        count += 1
t = int(input())
for ii in range(t):
    n = int(input())
    isSmith = False
    for smithNum in smith:
        if smithNum == n:
            isSmith = True
            break
    if isSmith:
        print(1)
    else:
        print(0)
