n = int(input())
time = 0
cuX = cuY = 0
first = 1
while n > 0:
    n -= 1
    str = input().split(",")
    tarX = int(str[0])
    tarY = int(str[1])
    if first == 1:
        first = 0
        cuX = tarX
        cuY = tarY
    if cuX == tarX and cuY == tarY:
        continue
    else:
        disX = abs(tarX-cuX)
        disY = abs(tarY-cuY)
        if disX > disY:
            time += disX
        else:
            time += disY
        cuX = tarX
        cuY = tarY
print(time)
