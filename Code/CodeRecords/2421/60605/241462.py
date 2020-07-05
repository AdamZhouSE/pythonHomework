def changeNum(string):
    newstr = ""
    for i in list(string):
        if i == "9":
            newstr = newstr + i
            continue
        newstr = newstr + "9"
        break
        
print(input().strip())