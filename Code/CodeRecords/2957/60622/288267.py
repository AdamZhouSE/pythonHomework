def solve(s,l):
    s=s[2:]
    offset=abs(len(s)-len(l))
    zero="0"*offset
    return zero+s
def W(l):
    n = len(l)
    son = []
    for i in range(n):
        for j in range(i, n):
            tem = []
            for k in range(i, j + 1):
                tem.append(l[k])
            if tem not in son:
                son.append(tem)
    return son
def Y(l):
    X = []
    for i in range(pow(2, len(l))):
        X.append(solve(bin(i),l))
    Mother = []
    for n in X:
        t = []
        for i in range(len(n)):
            if n[i] == '1':
                t.append(l[i])
        if t not in Mother and len(t) != 0:
            Mother.append(t)
    return Mother

p=list(input())
r=W(p)
print(r)
c=0
for element in r:
    A=W(element)
    B=Y(element)
    A.sort()
    B.sort()
    # print(A)
    # print(B)
    if A==B:
        # print(True)
        c+=1
    # print()
print(c)





