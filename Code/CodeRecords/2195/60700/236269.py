def intToBinary(i):
    """"十进制转二进制"""
    binary = []
    while i != 0:
        binary.append(i % 2)
        i //= 2
    return binary


def isPrime(n):
    """判断n是否为质数"""
    if n == 1:
        return False
    m = 2
    while m <= n/2:
        if n % m == 0:
            return False
        m += 1
    return True


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = nums[i].split(' ')
    l = int(num[0])
    r = int(num[1])
    count = 0
    for n in range(l, r+1):
        b = intToBinary(n)
        if isPrime(b.count(1)):
            count += 1
    print(count)
