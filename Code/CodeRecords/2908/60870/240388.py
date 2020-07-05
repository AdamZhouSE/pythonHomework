num = input()
allDict = {}
i = 0
while i < int(num):
    word_str = input()
    moduleDict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    for ch in word_str:
        if ch in moduleDict.keys():
            moduleDict[ch] = moduleDict[ch] + 1
    moduleDict_str = str(moduleDict)
    if moduleDict_str in allDict.keys():
        allDict[moduleDict_str] = allDict[moduleDict_str] + 1
    else:
        allDict[moduleDict_str] = 1
    i = i + 1
print(len(allDict), end = '')