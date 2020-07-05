temp1 = list(map(int, input().split()))
houses = [0 for x in range(0, temp1[0])]
d = []
result = []
for operate in range(0, temp1[-1]):
    operand = list(input().split())
    if operand[0] == "D":
        temp2 = int(operand[-1]) - 1
        d.append(temp2)
        houses[temp2] = -1
    elif operand[0] == "R":
        temp3 = d[-1]
        d = d[:-1]
        houses[temp3] = 0
    else:
        temp4 = int(operand[-1]) - 1
        if houses[temp4] == -1:
            result.append(0)
        else:
            count, i = 0, temp4
            while houses[i] != -1:
                count += 1
                i += 1
                if i == len(houses):
                    break
            i = temp4 - 1
            if i >= 0:
                while houses[i] != -1:
                    count += 1
                    i -= 1
                    if i <= 0:
                        break
            result.append(count)
for x in result:
    print(x)