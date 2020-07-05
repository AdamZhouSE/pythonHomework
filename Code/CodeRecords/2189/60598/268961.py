times = int(input())


def cal(a):
    string = str(a)
    result = 0
    for i in range(len(string)):
        result += int(string[i]) * int(string[i])
    return result


def check(num):
    fast = num
    isOne = True
    while num != 1:
        num = cal(num)
        fast = cal(fast)
        fast = cal(fast)
        if fast == 1:
            break
        if num == fast:
            isOne = False
            break
    return isOne


for i in range(times):
    num = int(input())
    nextNum = num + 1
    while 1:
        if check(nextNum):
            print(nextNum)
            break
        else:
            nextNum += 1

