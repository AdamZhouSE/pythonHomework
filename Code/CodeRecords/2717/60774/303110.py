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
        else:
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
    for e in equal:
        if(e in unequal):
            print('false')
            break
    else:
        if(equal != ['b==d']):
            print(equal)
            print(unequal) 
        print('true')