graph=eval(input())
branch=[]
for p in graph:
    if p[0] in branch and p[1] in branch:
        print(p)
        break
    else:
        if p[0] not in branch:
            branch.append(p[0])
        if p[1] not in branch:
            branch.append(p[1])
