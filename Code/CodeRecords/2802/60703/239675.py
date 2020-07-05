n,m=map(int,input().split());
numList=[int(x) for x in input().split()];
childList = [];

class child:
    n=0;
    id= 0;
    def __init__(self,num,idd):
        self.n=num;
        self.id =idd;

for i in range(0,len(numList)):
    childList.append(child(numList[i],i+1));
while(len(childList)!=1):
    childList[0].n-=m;
    if(childList[0].n<=0):
        childList = childList[1:];
    else:
        tempchild = childList[0];
        childList = childList[1:];
        childList.append(tempchild);


print(childList[0].id);