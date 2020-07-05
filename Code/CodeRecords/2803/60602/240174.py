def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def lightupLanterns(list,m):
    lanterns=[];
    while(m>0):
        lanterns.append(0);
        m-=1;
    list=makeIntList(list);
    i=0;
    while(i<len(list)):
        if(lanterns[list[i]-1]==0):
            lanterns[list[i]-1]=1;
        i+=1;
    for element in lanterns:
        if(element==0):
            print("NO");
            return
    print("YES");


Total=str(input());
Total=Total.split(" ");
i=0;
ans=[];
while(i<int(Total[0])):
    list=str(input());
    list=list.split(" ");
    j=1;
    while(j<len(list)):
        ans.append(list[j]);
        j+=1;
    i+=1;
lightupLanterns(ans,int(Total[1]));