n=int(input())
if n==1:
    print(4*int(input())+2)
else:
    list=[]
    for i in range(n):
        l=input().split(",")
        for j in range(n):l[j]=int(l[j])
        list.append(l)
    area=0
    maxRows=[]
    maxColumns=[]
    for i in range(n):
        maxRow=0
        maxColumn=0
        for j in range(n):
            if list[i][j]!=0: area+=2
            if list[i][j]>maxRow: maxRow=list[i][j]
            if list[j][i]>maxColumn: maxColumn=list[j][i]
        maxRows.append(maxRow)
        maxColumns.append(maxColumn)
    for e in maxRows: area+=2*e
    for e in maxColumns: area+=2*e
    if n==2:print(area)
    elif n==3:
        if list[0][1]>list[1][1]: area+=list[0][1]-list[1][1]
        if list[1][0]>list[1][1]: area+=list[1][0]-list[1][1]
        if list[1][2] > list[1][1]: area += list[1][2] - list[1][1]
        if list[2][1] > list[1][1]: area += list[2][1] - list[1][1]
        print(area)