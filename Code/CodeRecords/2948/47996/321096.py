str1 = input()
L = len(str1)
ST = int(input())
newStr = ""
for i in range(L):
    num = ord(str1[i]) - ord('A') + ST
    newStr += str(num)
while len(newStr) > 3:
    tempStr = ""
    length = len(newStr)
    for i in range(length-1):
        tempNum = int(newStr[i]) + int(newStr[i+1])
        if tempNum >= 10:
            tempNum -= 10
        tempStr += str(tempNum)
    newStr = tempStr
while int(newStr) > 100:
    tempStr = ""
    length = len(newStr)
    for i in range(length-1):
        tempNum = int(newStr[i]) + int(newStr[i+1])
        if tempNum >= 10:
            tempNum -= 10
        tempStr += str(tempNum)
    newStr = tempStr
print(int(newStr), end="")
