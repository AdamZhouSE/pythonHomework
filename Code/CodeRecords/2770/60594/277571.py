def findall(row,oc,final,jieshu):
    ky=[]
    for i in row:
        if i[0]>jieshu:
            ky.append(i)
    if len(ky)==0:
        final.append(oc)
    else:
        for i in ky:
            oc2=oc.copy()
            oc2.append(i)
            findall(row,oc2,final,i[1])
def findmax(oc):
    for i in range(len(oc)):
        for j in range(i+1,len(oc)):
            if len(oc[i])<len(oc[j]):
                tmp=oc[i]
                oc[i]=oc[j]
                oc[j]=tmp

n=int(input())
for i in range(n):
    a=int(input())
    row1=[int(n) for n in input().split()]
    row2=[int(n) for n in input().split()]
    row=[]
    for j in range(a):
        row.append([row1[j],row2[j]])
    final=[]
    findall(row,[],final,0)
    findmax(final)
    oc=[]
    for j in final[0]:
        oc.append(row.index(j)+1)
    for j in range(len(oc)):
        print(oc[j], end=' ')
    print()