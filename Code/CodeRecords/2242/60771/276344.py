#06
ori = input().split(",")
point1 = [int(item) for item in ori]
ori = input().split(",")
point2 = [int(item) for item in ori]
x1 = point2[0]
y1 = point2[1]
x2 = point1[0]
y2 = point1[1]
length = x2 - x1
width = y2 - y1
if length*width == 0:
    print(False)
else:
    print(True)