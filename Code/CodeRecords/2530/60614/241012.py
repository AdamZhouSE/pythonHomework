strS=input()
def cmp(first,second):
    if first in strS and second in strS:
        if first==second:
            return 0
        elif strS.index(first)<strS.index(second):
            return -1
        else:return 1
    else:
        return 0
listT=list(input())
for i in range(0,len(listT)-1):
    for j in range(len(listT)-1,i,-1):
        if cmp(listT[j],listT[j-1])<0:
            temp=listT[j]
            listT[j]=listT[j-1]
            listT[j-1]=temp
print("".join(listT))