def equationsPossible(equations: 'List[str]') -> 'bool':

    equ = []
    inequ = []
    for equation in equations:
        if "==" in equation:
            equation = equation.split("==")
            equ.append([equation[0], equation[-1]])
        else:
            equation = equation.split("!=")
            inequ.append([equation[0], equation[-1]])
    f = {}

    def find(x):
        f.setdefault(x, x)
        if x != f[x]:
            f[x] = find(f[x])
        return f[x]

    def union(x, y):
        f[find(x)] = find(y)

    for x, y in equ:
        union(x, y)
    # print(f)
    for i, j in inequ:
        # print(find(i),find(j))
        if find(i) == find(j):
            return 'false'
    print(equations)
    return 'true'
a=input()
li=a[1:len(a)-1].split(",")
rr=[]
for i in li:
    rr.append(i[1:len(i)-1])
print(equationsPossible(li))