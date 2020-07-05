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

def isInTri(p0, p1, p2, p3):
    a = getArea(p0, p1, p2)
    b = getArea(p0, p1, p3)
    c = getArea(p0, p2, p3)
    big = getArea(p1, p2, p3)

    if a == 0 or b == 0 or c == 0:
        return False

    if big == a + b + c:
        return True
    else:
        return False

def getpointlist(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)

    ctr = 0

    for i in range (min_x, max_x):
        for j in range (min_y, max_y):
            tmp = [i, j]
            if isInTri(tmp, point1, point2, point3):
                ctr += 1

    return ctr

if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        a = getInput()
        b = getInput()
        c = getInput()
        p = getpointlist(a, b, c)
        print(p);

