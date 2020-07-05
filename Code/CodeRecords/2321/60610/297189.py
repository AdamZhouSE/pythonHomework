string=input().split(",");
N=input();
result=0;
for i in range(1,len(N)):
    result+=pow(len(string),i);
mid=[];
l=list(map(int,string));
l=sorted(l);
cout=0;
j=len(l)-1;
i=0;
while(j>=0):
    if(l[len(l)-1]<int(N[i])):
        mid.append([len(N),0]);
        break;
    if(l[j]<int(N[i])):
        if(mid!=[]):
            if(mid[-1][1]!=1):
                mid.append([j+1,0]);
                break;
            else:
                mid[-1][1]-=1;
                break;
        else:
            mid.append([j+1,0]);
            break;
    elif(l[j]==int(N[i])):
        mid.append([j+1,1]);
        i+=1;
        j=len(l)-1;
    else:
        j-=1;
if(j==-1)&(mid[-1][1]==1):
    mid[-1][0]-=1;
count=0;
if(len(mid)!=0):
    count=1;
    for i in mid:
        count*=i[0];
    for i in range(len(N)-len(mid)):
        count*=len(l);
print(result+count)

