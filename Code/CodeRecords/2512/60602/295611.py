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
string=input().split(" ");
listsize=int(string[0]);
P=int(string[1]);
list=makeIntList(input().split(" "));
Total=int(input());
i=0;
while(i<Total):
    temp=makeIntList(input().split(" "));
    if(temp[0]==1):
        j=temp[1]-1;
        while(j<temp[2]):
            list[j]*=temp[3];
            j+=1;
    elif(temp[0]==2):
        j=temp[1]-1;
        while(j<temp[2]):
            list[j]+=temp[3];
            j+=1;
    elif(temp[0]==3):
        print(sum(list[temp[1]-1:temp[2]])%P);
    i+=1;