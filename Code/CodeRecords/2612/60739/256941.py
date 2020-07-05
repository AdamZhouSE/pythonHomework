import math

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def Manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = abs(x2 - x1) + abs(y2 - y1)

    return d

def Euclid(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = x2 - x1
    y = y2 - y1
    d = math.sqrt(pow(x, 2) + pow(y, 2))
    return d

def isEqual(p1, p2):
    if Manhattan(p1, p2) == Euclid(p1, p2):
        return True
    else:
        return False

def getNum(list):
    num = 0
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list) - 1):
            if isEqual(list[i], list[j]):
                num += 1
    return num

if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        m = int(input())
        list = []
        for j in range (m):
            tmp = getInput()
            list.append(tmp)
        p = getNum(list)
        print(p)
