tree=eval(input())
conti=True
for i in range(len(tree)-1,-1,-1):
    if not conti:
        break
    a=tree[i][1]
    for j in range(0,i):
        b=tree[j][1]
        if a==b:
            print(tree[i])
            conti=False
            break