size = int(input())
a = 0
while a < size:
    l = input().split()
    b = int(l[0])
    bStr = bin(b)
    resultStr = ""
    i = 0
    while i < len(bStr):
        if ((i >= len(bStr) - int(l[2])) and (i <= len(bStr) - int(l[1]))):
            if (bStr[i] == "0"):
                resultStr = resultStr + "1"
            else:
                resultStr = resultStr + "0"
        else:
            resultStr = resultStr + bStr[i]
        i = i + 1
    print(int(resultStr, 2))
    a = a + 1