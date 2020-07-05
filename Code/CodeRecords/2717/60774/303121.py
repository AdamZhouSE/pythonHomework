def combine(newEq,eqLst):
    k = len(eqLst)
    for k in range(0,k):
        if(newEq[0] == eqLst[k][0]):
            eqLst.append([newEq[1],eqLst[k][1]])
        elif(newEq[0] == eqLst[k][1]):
            eqLst.append([newEq[1],eqLst[k][0]])
        elif(newEq[1] == eqLst[k][0]):
            eqLst.append([newEq[0],eqLst[k][1]])
        elif(newEq[1] == eqLst[k][1]):
            eqLst.append([newEq[0],eqLst[k][0]])
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
        unequal = combine([eq[0],eq[3]],unequal)        
    else:
        equal = combine([eq[0],eq[3]],equal)
else:
    for e in equal:
        if([e[1],e[0]] in unequal or [e[0],e[1]] in unequal):
            print('false')
            break
    else:
        print('true')