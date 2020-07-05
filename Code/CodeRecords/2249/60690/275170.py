s=input()[2:-2]
s=s.split("],[")
list=[]
for i in range(len(s)):
    l=s[i].split(",")
    for j in range(len(l)):
        l[j]=int(l[j])
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