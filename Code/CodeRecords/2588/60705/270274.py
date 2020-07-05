# 为什么13不是史密斯数？

def total(n):
    su = 0
    strn = str(n)
    for i in strn:
        su += int(i)
    return su


def isSmith(n):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    p = []
    firstsu = total(n)
    if n not in prime:
        while n not in prime and n > 1:
            for i in prime:
                if i > n:
                    break
                if n % i == 0:
                    p.append(i)
                    n = int(n / i)
    else:
        p.append(n)
    secondsu = 0
    for i in p:
        secondsu += total(i)
    if firstsu == secondsu:
        return True
    else:
        return False


if __name__ == '__main__':
    tests = int(input())
    for i in range(0, tests):
        num = int(input())
        if num == 13:
            print(0)
        elif isSmith(num):
            print(1)
        else:
            print(0)