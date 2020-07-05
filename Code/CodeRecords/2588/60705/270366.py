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
    if n in prime
        p.append(n)
    else:
        while True:
            if n == 1:
                break
            for ir in prime:
                if n % ir == 0:
                    p.append(ir)
                    n = int(n/ir)


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