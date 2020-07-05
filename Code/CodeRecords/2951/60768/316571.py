str1 = input()
str2 = input()
int2 = int(str2, 3)
tempInt2 = 0
ZERO_ONE = [0, 1]
ONE_TWO = [1, 2]
ZERO_TWO = [0, 2]
for i in range(0, len(str2)):
    tempStr2 = str2
    if str2[i] == '0':
        for j in ONE_TWO:
            tempStr2 = str2[0:i] + str(j) + str2[i + 1:len(str2)]
            tempInt2 = int(tempStr2, 3)
            for m in range(len(str1)):
                tempStr1 = str1
                if tempStr1[m] == '1':
                    tempStr1 = str1[0: m] + '0' + str1[m + 1: len(str1)]
                else:
                    tempStr1 = str1[0: m] + '1' + str1[m + 1: len(str1)]

                tempInt1 = int(tempStr1, 2)
                if tempInt2 == tempInt1:
                    print(tempInt1, end="")
    elif str2[i] == '1':
        for j in ZERO_TWO:
            tempStr2 = str2[0:i] + str(j) + str2[i + 1:len(str2)]
            tempInt2 = int(tempStr2, 3)
            for m in range(0, len(str1)):
                tempStr1 = str1
                if tempStr1[m] == '1':
                    tempStr1 = str1[0: m] + '0' + str1[m + 1: len(str1)]
                else:
                    tempStr1 = str1[0: m] + '1' + str1[m + 1: len(str1)]

                tempInt1 = int(tempStr1, 2)
                if tempInt2 == tempInt1:
                    print(tempInt1, end="")
    else:
        for j in ZERO_ONE:
            tempStr2 = str2[0:i] + str(j) + str2[i + 1:len(str2)]
            tempInt2 = int(tempStr2, 3)
            for m in range(0, len(str1)):
                tempStr1 = str1
                if tempStr1[m] == '1':
                    tempStr1 = str1[0: m] + '0' + str1[m + 1: len(str1)]
                else:
                    tempStr1 = str1[0: m] + '1' + str1[m + 1: len(str1)]

                tempInt1 = int(tempStr1, 2)
                if tempInt2 == tempInt1:
                    print(tempInt1, end="")