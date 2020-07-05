def reverseStr(paramStr):
    for c in range(len(paramStr)):
        if paramStr[c].islower():
            char = chr(ord("z") - (ord(paramStr[c]) - ord("a")))
            paramStr = replace_char(paramStr, char, c)
        if paramStr[c].isupper():
            char = chr(ord("Z") - (ord(paramStr[c]) - ord("A")))
            paramStr = replace_char(paramStr, char, c)
    return paramStr


def replace_char(string, char, index):
    string = list(string)
    string[index] = char
    return ''.join(string)


inputLines = []
inputStr = ""
resultStr = []
result = ""
while inputStr != "!":
    inputStr = input()
    inputLines.append(inputStr)
for index in range(0, len(inputLines) - 1):
    resultStr.append(reverseStr(inputLines[index]))
for item in resultStr:
    result += item + "\n"
print(result.strip("\n"))
