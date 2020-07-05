def printLine(k, num):
    mid = int(num/2 + 1)
    if k > mid:
        printLine(2 * mid - k, num)
    else:
        numD = k * 2 - 1
        left = int((num - numD) / 2)
        s = left * '*' + numD * 'D' + left * '*'
        print(s)

def getDiamond(num):
    for i in range (num):
        printLine(i + 1, num)


n = int(input())
getDiamond(n)