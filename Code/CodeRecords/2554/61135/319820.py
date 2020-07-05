size=0
lis=[]
while(size<10000):
    lis.append(0)
    size+=1
Total=int(input())
x=0
saverList=[]
class cowSaver:
    def __init__(self,i,j):
        self.i=i
        self.j=j
def examCowSaver(list,Saver):
    count=0
    x=Saver.i-1
    while(x<Saver.j-1):
        list[x]-=1
        x+=1
    y=0
    while(y<len(list)):
        if(list[y]!=0):
            count+=1
        y+=1
    return count
while(x<Total):
    temp=input().split(" ")
    temp=list(int(a) for a in temp)
    i=temp[0]
    j=temp[1]
    saverList.append(cowSaver(i,j))
    y=i-1
    while(y<j-1):
        lis[y]+=1
        y+=1
    x+=1
x=0
ans=0
while(x<len(saverList)):
    z=0
    tempList=[]
    while(z<len(lis)):
        tempList.append(lis[z])
        z+=1
    tempNum=examCowSaver(tempList,saverList[x])
    if(tempNum>ans):
        ans=tempNum
    x+=1
print(ans,end="")