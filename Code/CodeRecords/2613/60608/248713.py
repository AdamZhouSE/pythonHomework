def getOdd(array, para1, para2):
    for i in range(0, para1):
        while para2 % 2 == 0:
            para2 += 1
        array.append(para2)
        para2+=2


def getEven(array, para1, para2):
    for i in range(0, para1):
        while para2 % 2 != 0:
            para2 += 1
        array.append(para2)
        para2+=2


def func19():
    times: int = eval(input())
    while times > 0:
        times -= 1
        n: int = eval(input())
        res = [1]
        num = 2
        while len(res) < n:
            getEven(res, num, res[-1] + 1)
            num += 1
            getOdd(res, num, res[-1] + 1)
            num += 1
        for i in range(0, n):
            if i == n - 1:
                print(res[i])
            else:
                print(res[i], end=" ")


func19()
