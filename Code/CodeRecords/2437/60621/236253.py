a=[int(x) for x in input().split()]
N,K=a[0],a[1]
netCollector=[]
position=0;
def takesecond(ele):
    return ele[0]
for i in range(N):
    temp=input().split()
    if(temp[1]=="L"):
        netCollector.append([position-int(temp[0]),1])
        netCollector.append([position,-1])
        position=position-int(temp[0])
    else:
        netCollector.append([position , 1])
        netCollector.append([position+int(temp[0]), -1])
        position=position+int(temp[0])
netCollector.sort(key=takesecond)
size=0;count=0
head=netCollector[0][0]
for i,j in enumerate(netCollector):
    if(j[1]==1):
        size+=1
        if size==K:
            head=j[0]
    else:

        if size==K:
            count+=(j[0]-head)
        size -= 1
print(count,end="")