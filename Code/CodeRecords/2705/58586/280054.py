edges=eval(input())
used=[]
for e in edges:
    if len(used)==0:
        used.append(e[0])
        used.append(e[1])
    else:
        if e[0] in used and e[1] in used:
            print(e)
            break
        elif e[0] in used:
            used.append(e[1])
        else:
            used.append(e[0])