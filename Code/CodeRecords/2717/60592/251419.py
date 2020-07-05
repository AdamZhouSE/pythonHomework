equ = eval(input())
equg = []
correct = 1
for i in range(0,len(equ)):
    mark1 = equ[i][1]
    mark2 = equ[i][2]
    alp1 = equ[i][0]
    alp2 = equ[i][3]
    inn1 = -1
    inn2 = -1
    if mark1 == mark2 =='=':
        tem = []
        for j in range(0,len(equg)):
            if alp1 in equg[j]:
                inn1 = j
            if alp2 in equg[j]:
                inn2 = j
        if inn1 == inn2:
            if inn1 == -1:
                equg.append([alp1,alp2])
            continue
        else:
            if inn1 != inn2 and inn1!=-1 and inn2 != -1:
                correct = 0
                break
            elif inn1 == -1:
                equg[inn2].append(alp1)
            else:
                equg[inn1].append(alp2)
    else:
        for j in range(0,len(equg)):
            if alp1 in equg[j]:
                inn1 = j
            if alp2 in equg[j]:
                inn2 = j
        if inn1 == inn2 and inn1 != -1:
            correct = 0
            break
        elif inn1 == inn1 and inn1 == -1:
            equg.append([alp1])
            equg.append([alp2])
        elif inn1!= inn2:
            if inn1 == -1:
                equg.append([alp1])
            elif inn2 == -1:
                equg.append([alp2])
if correct:
    print("true")
else:
    print("false")