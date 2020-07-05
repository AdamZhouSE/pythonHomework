import math


def isPrime(m):
    j = 2
    if m == 2:
        return True
    while j < int(math.sqrt(m)) + 1:
        if m % j == 0:
            return False
        j += 1
    return True


num = int(input())
for i in range(num):
    m = int(input())
    j = 2
    ans = []
    flag = False
    while j < int(m/2)+1:
        if isPrime(j):
            if m % j == 0:
                ans.append(j)
        j += 1
        if len(ans) == 3 and ans[0] * ans[1] * ans[2] == m:
            print(1)
            flag = True
            break
    if flag:
        continue
    print(0)
