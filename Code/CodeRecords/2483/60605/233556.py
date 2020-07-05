cnt = int(input())
liStr = []
liPatt = []
for i in range(cnt):
    liStr.append(input())
    liPatt.append(input())

for i in range(cnt):
    isIn = False
    for j in list(liStr[i]):
        if j in list(liPatt[i]):
            print(j)
            isIn = True
            break
    if not isIn:
        print("$")