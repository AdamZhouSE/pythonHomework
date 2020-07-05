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
    ab = nums[i].split(' ')
    sum = int(ab[0]) + int(ab[1])
    c = 1
    while not isPrime(sum + c):
        c += 1
    print(c)
