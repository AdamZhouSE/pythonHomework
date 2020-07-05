init=[int(x) for x in input().split()]
chart=[]
instr=[]
for i in range(init[0]):
    chart.append(input())
for i in range(init[2]):
    instr.append([int(x) for x in input().split()])
for i in instr:
    subchart=[]
    for j in range(i[0]-1,i[2]):
        subchart.append(chart[j][i[1]-1:i[3]])
    disjointSetUnion=[0]*((i[3]-i[1]+1)*(i[2]-i[0]+1))
    for j in range(i[2]-i[0]+1):
        for k in range(i[3]-i[1]+1):
            if subchart[j][k]=='1':
                disjointSetUnion[j*(i[3]-i[1]+1)+k]=j*(i[3]-i[1]+1)+k
            else:
                disjointSetUnion[j*(i[3]-i[1]+1)+k]=-1
    for j in range(0,i[2]-i[0]+1):
        for k in range(0,i[3]-i[1]+1):
            if k!=i[3]-i[1]:
                if subchart[j][k]=='1' and subchart[j][k+1]=='1':
                    temp=disjointSetUnion[j*(i[3]-i[1]+1)+k+1]
                    while temp in disjointSetUnion:
                        disjointSetUnion[disjointSetUnion.index(temp)]=disjointSetUnion[j*(i[3]-i[1]+1)+k]
            if j!=i[2]-i[0]:
                if subchart[j][k]=='1' and subchart[j+1][k]=='1':
                    temp=disjointSetUnion[(j+1)*(i[3]-i[1]+1)+k]
                    while temp in disjointSetUnion:
                        disjointSetUnion[disjointSetUnion.index(temp)]=disjointSetUnion[j*(i[3]-i[1]+1)+k]
    count=0
    while -1 in disjointSetUnion:
        disjointSetUnion.remove(-1)
    while len(disjointSetUnion)>0:
        key=disjointSetUnion.pop(0)
        count+=1
        while key in disjointSetUnion:
            disjointSetUnion.remove(key)
    print(count)
