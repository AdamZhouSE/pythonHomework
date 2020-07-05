def onOneLine(coordinates):

    pointONE = coordinates[0]
    pointTWO = coordinates[1]
    k = (pointONE[1] - pointTWO[1]) / (pointONE[0] - pointTWO[0])
    b = pointONE[1] - k * pointONE[0]

    for i in coordinates:
        if i[1] != k * i[0] + b:
            return False
    return True


nums = int(input())
coordinates = []
for i in range(0, nums):
    row = input().split(',')
    row[0] = int(row[0])
    row[1] = int(row[1])
    coordinates.append(row)
over = False
for i in range(0, nums - 1):
    for j in range(i + 1, nums):
        if coordinates[i] == coordinates[j]:
            print(False)
            over = True
            break
    if over:
        break
if not over:
    if onOneLine(coordinates):
        print(False)
    else:
        print(True)