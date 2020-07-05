def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        try:
            ans.append(int(list[count]));
        except Exception as e:
            count+=1;
            continue;
        count += 1;
    return ans;
stringSize=makeIntList(input().split(" "));
n=stringSize[0];
m=stringSize[1];
i=0;
list=[];
while(i<n):
    list.append("");
    i+=1;
i=0;
model="a";
while(i<m):
    temp=makeIntList(input().split(" "));
    JUDGE=temp[0];
    L=temp[1];
    R=temp[2];
    if(JUDGE==1):
        j=L-1;
        while(j<R):
            list[j]+=model;
            j+=1;
        model=chr(ord(model)+1);

    elif(JUDGE==2):
        j=L-1;
        tempS = ""
        while(j<R):
            x=0;
            while(x<len(list[j])):
                if(list[j][x] not in tempS):
                    tempS+=list[j][x];
                x+=1;
            j+=1;
        print(len(tempS));

    i+=1;