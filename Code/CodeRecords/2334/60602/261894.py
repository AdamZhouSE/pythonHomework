def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def maxTriangleC(list):
    list=makeIntList(list);
    i=0;
    ans=[];
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            x=j+1;
            while(x<len(list)):
                temp=[];
                temp.append(list[j]);
                temp.append(list[i]);
                temp.append(list[x]);
                tempMax=max(temp);
                temp.remove(max(temp));
                if(temp[0]+temp[1]>tempMax):
                    ans.append(list[j]+list[i]+list[x]);
                x+=1;
            j+=1;
        i+=1;

    if(ans==[]):
        print(0);
    else:
        print(max(ans));





C=str(input()).split(",");
maxTriangleC(C);