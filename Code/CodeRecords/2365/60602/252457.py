def biggestNum(list,ans):
    if(list!=[]):
        i=0;
        biggest=list[0];
        temp=0;
        while(i<len(list)):
            if(temp>=len(list[i])or temp>=len(biggest)):
                if(list[i][len(list[i])-1]>list[i][len(list[i])-2]):
                    biggest=list[i];
                temp=0;
                i+=1;
                continue;
            if(list[i][temp]>biggest[temp]):
                biggest=list[i];
                temp=0;
            elif(list[i][temp]==biggest[temp]):
                temp+=1;
                i-=1;
            else:
                temp=0;
            i+=1;
        ans+=biggest;
        list.remove(biggest);
        return biggestNum(list,ans);
    else:
        return ans;






Total=int(input());
while(Total>0):
    temp=int(input());
    list=str(input());
    list=list.split(" ");
    print(biggestNum(list,""));
    Total-=1;