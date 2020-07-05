init=eval(input())
def cmp(x):
    if x[1]=='=':
        return 0
    else:
        return 1
init.sort(key=lambda x:cmp(x))
groups=[]
judge=True
for i in init:
    if i[1]=='=':
        firstInGroups = False
        for j in groups:
            if i[0] in j:
                firstInGroups=True
                if i[3] not in j:
                    for k in groups:
                        if i[3] in k:
                            judge=False
                            break
                    if judge:
                        j.append(i[3])
                    else:
                        break
                else:break
        if not firstInGroups:
            secondInGroups=False
            for j in groups:
                if i[3] in j:
                    secondInGroups=True
                    j.append(i[0])
                    break
            if not secondInGroups:
                groups.append([i[0],i[3]])
        if not judge:
            break
    else:
        for j in groups:
            if i[0] in j and i[3] in j:
                judge=False
                break
if judge:
    print("true")
else:
    print("false")