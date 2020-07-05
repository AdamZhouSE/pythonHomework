def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def getArea(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    Area = abs((x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)) / 2
    return Area

def getRectArea(p1, p2, p3, p4):
    a = getArea(p1, p2, p3)
    b = getArea(p1, p4, p3)
    return a + b

def isInRect(p0, p1, p2, p3, p4):
    a = getArea(p0, p1, p2)
    b = getArea(p0, p1, p4)
    c = getArea(p0, p2, p3)
    d = getArea(p0, p3, p4)
    big = getRectArea(p1, p2, p3, p4)


    if big == a + b + c + d:
        return True
    else:
        return False
def getNum(point_list, p1, p2, p3, p4):
    num = 0
    for i in point_list:
        if isInRect(i, p1, p2, p3, p4):
            print('YES')
        else:
            print('NO')
    return num

p = getInput()
n = p[0]
d = p[1]
p1 = [0,d]
p2 = [d,0]
p3 = [n,n-d]
p4 = [n-d, n]

num = int(input())
point_list = []
for i in range(num):
    point_list.append(getInput())

k = getNum(point_list, p1, p2, p3, p4)
