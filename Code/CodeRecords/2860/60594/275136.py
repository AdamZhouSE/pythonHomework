n=int(input())
xuedui=[]
for i in range(n):
    row=[int(n) for n in input().split()]
    xuedui.append(row)
xiangdeng=[[xuedui[0]]]
for i in range(1,n):
    cunzai=False
    for j in range(len(xiangdeng)):
        for k in range(len(xiangdeng[j])):
            if xiangdeng[j][k][0]==xuedui[i][0] or xiangdeng[j][k][1]==xuedui[i][1]:
                xiangdeng[j].append(xuedui[i])
                cunzai=True
                break
        if cunzai==True:
            break
    if cunzai==False:
        new=[]
        new.append(xuedui[i])
        xiangdeng.append(new)
print(len(xiangdeng)-1)

