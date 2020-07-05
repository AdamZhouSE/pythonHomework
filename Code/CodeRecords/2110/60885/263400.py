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

num = int(input())
result = isUgly(num)
print(result)
            