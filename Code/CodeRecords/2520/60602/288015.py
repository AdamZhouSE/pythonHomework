class Point:

    def __init__(self,r,c,r0,c0):
        self.r=r;
        self.c=c;
        self.distance=abs(r-r0)+abs(c-c0);

R=int(input());
C=int(input());
r0=int(input());
c0=int(input());

i=0;
list=[];
while(i<R):
    j=0;
    while(j<C):
        list.append(Point(i,j,r0,c0));
        j+=1;
    i+=1;

disList=[];
i=0;
while(i<len(list)):
    disList.append(list[i].distance);
    i+=1;

disList=sorted(disList);
ans=[];

while(len(disList)!=0):
    i = 0;
    while(i<len(list)):
        if(list[i].distance==disList[0]):
            ans.append([]);
            ans[len(ans)-1].append(list[i].r);
            ans[len(ans) - 1].append(list[i].c);
            disList.remove(disList[0]);
            list.remove(list[i]);
            break;
        i+=1;

print(ans);