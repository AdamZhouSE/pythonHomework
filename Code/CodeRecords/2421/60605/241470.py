def changeNum(string):
    newstr = ""
    isOK = True
    for i in list(string):
        if i == "6" and isOK:
            newstr = newstr + "9"
            isOK = False
        else:
            newstr = newstr + i
            continue
    return newstr

print(changeNum(input().strip()))