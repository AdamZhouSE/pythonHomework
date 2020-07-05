stringM = input()
stringS = input()
length = len(stringS)
while stringM.find(stringS) != -1:
    index = stringM.find(stringS)
    stringM = stringM[: index] + stringM[index + length:]
print(stringM)