express=input()
leftBracket,rightBracket=[0,0]
result,sybmol=[True,True]
for i in range(len(express)):
    if express[i]=="(":
        leftBracket+=1
    if express[i]==")":
        rightBracket+=1
        if leftBracket <rightBracket:
            sybmol=False
            break

if sybmol==False:
    print("NO",end="")
else :
    if leftBracket==rightBracket:
        print("YES",end="")
    else:
        print("NO",end="")