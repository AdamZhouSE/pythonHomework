equations=eval(input())
linked=[]
used=[]
while True:
    temp=[]
    for i in range(len(equations)):
        if i not in used:
            if equations[i][1]=="=":
                if len(temp)==0:
                    temp.append(equations[i][0])
                    temp.append(equations[i][3])
                    used.append(i)
                flag=True
                while flag:
                    flag=False
                    for i in range(len(equations)):
                        if i not in used:
                            if equations[i][1]=="=":
                                if equations[i][0] in temp and equations[i][3] not in temp:
                                    temp.append(equations[i][3])
                                    flag=True
                                    used.append(i)
                                elif equations[i][3] in temp and equations[i][0] not in temp:
                                    temp.append(equations[i][0])
                                    flag=True
                                    used.append(i)
    if len(temp)==0:
        break
    else:
        linked.append(temp)
def isValid(linked,equations):
    for e in equations:
        if e[1]=="!":
            for l in linked:
                if e[0] in l and e[3] in l:
                    return False
    return True
res=isValid(linked,equations)
if res:
    print("true")
else:
    print("false")