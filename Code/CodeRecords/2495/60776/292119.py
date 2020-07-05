str=input()
a=input()
a=a.replace("[\"","")
a=a.replace("\"]","")
b=a.split("\",\"")
b.sort(key=lambda x:len(x),reverse=True)
isright=1
for i in range(0,len(b)):
    c=str
    for j in range(0,len(b[i])):
        if b[i][j] in c:
            c.replace(b[i],"",1)
        else:
            isright=0
            break
    if isright==1:
        print(b[i])
        break
    else:
        isright=1