def solution(equations) ->str :
    equal = set()
    alph=set()
    for eq in equations:
        if eq[1] == '=' :
            equal.add(eq)
            alph.add(eq[0])
            alph.add(eq[3])
    unequal=set(equations).difference(equal)
    for i in unequal:
        if i[0] in alph and i[3] in alph:
            return "false"
    return "true"

if __name__=="__main__":
    equations = eval(input())
    res=solution(equations)
    print(res)