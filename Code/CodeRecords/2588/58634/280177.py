def divPrime(num):
    lt = []
    while num != 1:
        for i in range(2, int(num + 1)):
            if num % i == 0:  # i是num的一个质因数
                lt.append(i)
                num = num / i  # 将num除以i，剩下的部分继续分解
                break
    return lt

def getSum(nums):
    res = 0
    for i in nums:
        temp = list(str(i))
        for j in temp:
            res += int(j)
    return res

t = int(input())
for i in range(t):
    n = int(input())
    if getSum([n]) == getSum(divPrime(n)):
        print(1)
    else:
        print(0)