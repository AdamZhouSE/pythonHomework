import math

T = int(input())


def turnToBinary(x):
    result = ""
    while x != 0:
        remain = x % 2
        x = int(math.floor(x / 2))
        result = str(remain) + result
    return result


def binaryToInt(string):
    count = 0
    for i in range(0, len(string)):
        if string[len(string) - i - 1] == "1":
            count = count + pow(2, i)
    return count


for i in range(0, T):
    num = int(input())
    binaryOfNum = turnToBinary(num)
    newString=binaryOfNum.replace("0","1")
    newNum=binaryToInt(newString)
    gap=newNum-num
    print(str(gap)+" "+str(newNum))
