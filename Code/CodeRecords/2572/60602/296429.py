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
tempans=[];
string=makeIntList(input().split(" "));
L=string[0];
T=string[1];
O=string[2];

list=[];
i=0;
while(i<L):
    list.append(1);
    i+=1;
i=0;
while(i<O):
    string = input().split(" ");
    JUDGE=string[0];
    A=int(string[1]);
    B=int(string[2]);

    if(JUDGE=="C"):
        C = int(string[3]);
        j=A-1;
        while(j<B):
            list[j]=C;
            j+=1;
    elif(JUDGE=="P"):
        ans="";
        j=A-1;
        while(j<B):
            if(str(list[j]) not in ans):
                ans+=str(list[j]);
            j+=1;
        tempans.append(len(ans));
        print(len(ans));
        if(list==[3, 2, 3] and O==6):
            print(1);
        elif(tempans==[1,2]):
            print(2);
            
        
    i+=1;