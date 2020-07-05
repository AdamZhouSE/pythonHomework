record = dict()


def cal(n, dictory):
    if n == 2 or n == 0:
        return 1
    elif n in dictory:
        return dictory[n]
    else:
        result = 0
        for i in range(int(n/2)):
            result += cal(i*2, dictory) * cal(n-2-i*2, dictory)
        dictory[n] = result
        return result


times = int(input())
for j in range(times):
    num = int(input())
    if num % 2 != 0:
        num -= 1
    print(cal(num, record))
