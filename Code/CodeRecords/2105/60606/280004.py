import math


def area(x1, y1, x2, y2):
    result = math.fabs(x1 - x2) * math.fabs(y1 - y2)
    return int(result)


array = input().split(", ")
array = [int(x) for x in array]
x1 = array[0]
y1 = array[1]
x2 = array[2]
y2 = array[3]
x3 = array[4]
y3 = array[5]
x4 = array[6]
y4 = array[7]
result = 0
if x3 <= x2 and y3 <= y2<y4:
    result = math.fabs(x2 - x3) * math.fabs(y3 - y2)
elif x3 < x2 and y4 > y1 > y3:
    result = math.fabs(x2 - x3) * math.fabs(y4 - y1)
elif x1 < x4 and y4>y2 > y3:
    result = math.fabs(x1 - x4) * math.fabs(y3 - y2)
elif x4 > x1 and y2>y4 > y1:
    result = math.fabs(x1 - x4) * math.fabs(y4 - y1)
temp = int(result)
result = 0
# 至此算出了重叠部分的面积
result += area(x1, y1, x2, y2)
result += area(x3, y3, x4, y4)
result-=temp
result = int(result)
print(result)
