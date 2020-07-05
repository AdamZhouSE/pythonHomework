testNum = int(input())
strs = []
patts = []
for i in range(0, testNum):
    strs.append(input())
    patts.append(input())
for i in range(0, len(strs)):
    theStr = strs[i]
    thePatt = patts[i]
    minIndex = 9999
    for j in range(0, len(thePatt)):
        #theChar = thePatt[i]
        for k in range(0, len(theStr)):
            if theStr[k] == thePatt[j] and k < minIndex:
                minIndex = k
    if minIndex == 9999:
        print("$")
    else:
        print(theStr[minIndex])print(input())
print(input())
print(input())
print(input())