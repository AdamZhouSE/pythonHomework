from math import sqrt
def test():
    n = int(input())
    if n<=1:
        print(False)
        return 
    factor = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if i not in factor:
                factor.append(i)
            if int(n / i) not in factor:
                factor.append(int(n / i))
    sum = 0
    for j in range(0, len(factor)):
        sum = sum + factor[j]
    if sum == n:
        print(True)
    else:
        print(False)


test()


