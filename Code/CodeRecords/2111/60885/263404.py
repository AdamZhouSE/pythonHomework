def isUgly(num):
    cands = [2,3,5]
    while num > 1:
        for n in cands:
            if num % n == 0:
                num /= n
                break
        else:
            return False
    return True

n = int(input())
i = 0
while n > 0:
    i += 1
    while not isUgly(i):
        i += 1
    n -= 1
print(i)