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
stringSize=input().split(" ");
N=int(stringSize[0]);
M=int(stringSize[1]);
i=0;
list=[];
while(i<N):
    list.append(False);
    i+=1;
i=0;
while(i<M):
    temp=makeIntList(input().split());
    a = temp[1];
    b = temp[2];
    if(temp[0]==0):
        j=a-1;
        while(j<b):
            list[j]=not list[j];
            j+=1;
    elif(temp[0]==1):
        j=a-1;
        count=0;
        while(j<b):
            if(list[j]):
                count+=1;
            j+=1;
        print(count);
    i+=1;