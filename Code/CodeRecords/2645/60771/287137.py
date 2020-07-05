#16
import math

bananas = eval(input())
H = int(input())
oriNum = math.floor(sum(bananas)/H)

while True:
    b = bananas[:]
    j = 0
    h = 0
    while True:
        if b[j] > 0:
            b[j] -= oriNum
            h += 1
        else:
            j += 1
        if h == H:
            break
    again = False
    # print(b)
    for item in b:
        if item > 0:
            again = True
    if again == False:
        break
    else:
        oriNum += 1

print(oriNum)
