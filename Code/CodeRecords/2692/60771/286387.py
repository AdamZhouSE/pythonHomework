#06
import math
weights = eval(input())
D = int(input())

oriNum = math.floor(sum(weights)/D)

while True:
    i = 0
    # print("oriNum: ",oriNum)
    for j in range(0,D):
        # print("j: ",j)
        total = 0
        part = []
        while total < oriNum and i < len(weights):
            # print("first i: ",i)
            total += weights[i]
            part.append(weights[i])
            i += 1
            # print(part)
            # print("Now total:",total)
        if total > oriNum:
            i -= 1
    # print("last: ",i)
    if i > len(weights)-1:
        break
    else:
        oriNum += 1
print(oriNum)


