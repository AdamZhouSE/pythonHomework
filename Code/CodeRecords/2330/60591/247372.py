import math
def isRec(points):
    if(points[0][0] == points[1][0]):
        if(points[2][0]!=points[3][0]):
            return False
        else:
            if(points[1][1]==points[3][1]):
                if(points[0][1] != points[2][1]):
                    return False
                else:
                    return True
            else:
                return False
    if (points[1][1] == points[3][1]):
        if (points[0][1] != points[2][1]):
            return False
        else:
            if (points[0][0] == points[1][0]):
                if (points[2][0] != points[3][0]):
                    return False
                else:
                    return True
            else:
                return False
    k1 = (points[0][1] - points[1][1]) / (points[0][0]- points[1][0])
    k2 = (points[0][1] - points[2][1]) / (points[0][0] - points[2][0])
    if(points[1][0]==points[3][0]):
        return False
    k3 = (points[1][1] - points[3][1]) / (points[1][0] - points[3][0])
    if (points[2][0] == points[3][0]):
        return False
    k4 = (points[2][1] - points[3][1]) / (points[2][0] - points[3][0])
    if(k1*k2 == -1 and k3*k4 == -1 and k1 * k3 == -1 and k2 * k4 == -1):
        return True
    else:
        return False

def cal(points):
    line1 = math.sqrt(pow(points[1][0] - points[0][0],2) + pow(points[1][1] - points[0][1],2))
    line2 = math.sqrt(pow(points[3][0] - points[1][0],2) + pow(points[3][1] - points[1][1],2))
    return line1 * line2

n = eval(input())
points = []
while(n != 0):
    n = n - 1
    point = list(map(int,input().split(",")))
    points.append(point)
points.sort()

count = 100000
for x in range(len(points)):
    for y in range(x + 1,len(points)):
        for z in range(y + 1,len(points)):
            for t in range(z + 1,len(points)):
                temp = [points[x],points[y],points[z],points[t]]
                if(isRec(temp)):
                    res = cal(temp)
                    if(res < count):
                        count = res
if(count == 100000):
    print("0.0000")
else:
    print("%.4f" %(count))