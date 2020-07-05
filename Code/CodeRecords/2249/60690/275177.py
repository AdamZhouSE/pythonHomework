n=int(input())
if n==1:
    print(int(input())*2+1)
else:
    list=[]
    for i in range(n):
        l=input().split(",")
        for i in range(len(l)): l[i]=int(l[i])
        list.append(l)

    xy,xz,yx=0,0,0
    maxRow=[]
    maxColumn=[]
    for i in range(len(list)):
        maxr,maxc=0,0
        for j in range(len(list[i])):
            if list[i][j]!=0: xy+=1
            if maxr<list[i][j]: maxr=list[i][j]
            if maxc<list[j][i]: maxc=list[j][i]
        maxRow.append(maxr)
        maxColumn.append(maxc)
    res=0
    for e in maxRow: res+=e
    for e in maxColumn: res+=e
    res+=xy
    print(res)