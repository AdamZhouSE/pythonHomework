size = int(input())
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
d = {}
for var in intList:
    if var in d.keys():
        d[var] += 1
    else:
        d[var] = 1
l = sorted(d.keys())
realD = {}
for i in l:
    realD[i] = d[i]
resultD = {}
resultD[1] = 0
resultD[-1] = 0
resultD[0] = 0
result = 0
for key, values in realD.items():
    temp = key
    tem = 0
    while abs(temp) != 1:
        if temp < 0:
            temp += 1
            tem += 1
        elif temp > 0:
            temp -= 1
            tem += 1
        else:
            break
    result += tem * values
    if temp == 1:
        resultD[1] += values
    elif temp == 0:
        resultD[0] += values
    else:
        resultD[-1] += values
signal = 1
for key, values in resultD.items():
    if key == -1 or key == 1:
        signal *= (key ** values)
if signal == 1:
    print(result + resultD[0])
else:
    if resultD[0] == 0:
        print(result + 2)
    else:
        print(result + resultD[0])
