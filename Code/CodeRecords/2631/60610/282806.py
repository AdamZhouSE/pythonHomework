string=input().split();
result=[0 for i in range(int(string[0])+1)];
mid=[];
for i in range(int(string[0])):
    string1=list(map(int,input().split()));
    mid.append(string1);
mid=sorted(mid);
count=0;
maxcow=-1;
for i in mid:
    result[i[1]-1]=result[i[1]-1]+i[2];
    if(result.index(max(result))!=maxcow):
        maxcow=result.index(max(result));
        count+=1;
print(count,end="");
