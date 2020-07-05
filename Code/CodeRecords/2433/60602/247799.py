def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def setToge(list):
    i=0;
    while(i<len(list)):
        j=i;
        while(j<len(list)):
            if(list[j][0]<=list[i][1] and i!=j):
                list[i][1]=list[j][1];
                list.remove(list[j]);
            j+=1;
        i+=1;
    print(list);
    return
list=[];
temp=str(input());
i=0;
ans=[];
while(i<len(temp)):
    if(temp[i]>='0' and temp[i]<='9'):
        if (temp[i+1] >= '0' and temp[i+1] <= '9'):
            list.append(int(temp[i])*10+int(temp[i+1]));
            i+=1;
        else:
            list.append(temp[i]);
    i+=1;
i=0;
while(i<len(list)):
    temp=[];
    temp.append(list[i]);
    temp.append(list[i+1]);
    temp=makeIntList(temp);
    ans.append(temp);
    i+=2;

setToge(ans);