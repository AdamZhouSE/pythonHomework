def is_sat(equations):
    dic_not_equal,dic_equal={},{}
    for e in equations:
        if e[1]=='!':
            if e[0]==e[3]:return False
            dic_not_equal[e[0]]=dic_not_equal.get(e[0],[])+[e[3]]
            dic_not_equal[e[3]] = dic_not_equal.get(e[3],[])+[e[0]]
        else:
            if e[0]==e[3]:continue
            dic_equal[e[0]]=dic_equal.get(e[0],[])+[e[3]]
            dic_equal[e[3]] = dic_equal.get(e[3],[])+[e[0]]

    for x in dic_not_equal.keys():
        if dic_equal.__contains__(x):
            for y in dic_not_equal.get(x):
                if y in dic_equal.get(x):
                    return False

    return True

equ=eval(input())
res=is_sat(equ)
if res:print('true')
else:print('false')