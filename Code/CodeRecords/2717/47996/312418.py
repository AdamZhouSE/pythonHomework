def equationsPossible(equations):
    tmp = {chr(i): chr(i) for i in range(97, 125)}
    
    def find(x):
        if x != tmp[x]:
            tmp[x]= find(tmp[x])
        return tmp[x]
    
    for it in equations:
        if it[1] == '=':
            tmp[find(it[0])] = find(it[-1])
            
    for it in equations:
        if it[1] == '!':
            if find(it[0]) == find(it[-1]):
                return False
    return True

str = input()[1:-1].split(",")
str = [x[1:-1] for x in str]
judge = equationsPossible(str)
if judge:
    print("true")
else:
    print("false")
