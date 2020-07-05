import math
class Point:

    def __init__(self,r,c):
        self.r=r;
        self.c=c;
        self.distance=math.sqrt(r*r+c*c);


def arrSort(arr1,arr2):
    i=0;
    ans=[];
    while(i<len(arr2)):
        j=0;
        while(j<len(arr1)):
            if(arr1[j]==arr2[i]):
                ans.append(arr1[j]);
                arr1.remove(arr1[j]);
                j-=1;
            j+=1;
        i+=1;

    ans+=sorted(arr1);
    print(ans);

temp=eval(input());
size=int(input());
i=0;
list=[];
while(i<len(temp)):
    list.append(Point(temp[i][0],temp[i][1]));
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

print(ans[0:size]);