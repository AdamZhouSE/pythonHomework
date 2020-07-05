a=input()

b=input()
isright="YES"
for i in range(0,len(b)):
    if b[i]!=' ':
        if b[i] in a:
            a.replace(b[i],"")
        else:
            isright = "NO"
print(isright,end="")