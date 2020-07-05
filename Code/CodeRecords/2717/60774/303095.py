def combine(newEq,eqLst):
    k = len(eqLst)
    for k in range(0,k):
        if(newEq[0] in eqLst[k] and newEq != eqLst[k]):
            eqLst[k].append(newEq[1])
    eqLst.append(newEq)
    return eqLst

equations = eval(input())
equal = []
unequal = []
for eq in equations:
    if(eq[0] == eq[3] and eq[1] == '!'):
        print('false')
        break
    elif(eq[0] == eq[3] and eq[1] == '='):
        continue
    elif(eq[1] == '!'):
        unequal = combine(eq,unequal)
    else:
        equal = combine(eq,equal)
else:
    flag = True
    for e1 in unequal:
        for e2 in equal:
            for sym in e1:
                if(sym not in e1):
                    break
            else:
                flag = False
                break
    if(flag):   
        print('true')
    else:
        print('false')