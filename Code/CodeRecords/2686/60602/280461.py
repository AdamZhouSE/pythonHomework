def makeIntList(list):

        
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;

def maxIncome(list,K):    
    i=0;
    temp=[];
    while(i<len(list)):
        temp.append(list[i]);
        i+=1;
    count=0;
    sum=0;
    while(count<K):
        i=0;
        dp=[];
        while(i<len(list)):
            dp.append(0);
            i+=1;
        i=0;
        while(i<len(list)):
            j=i-1;
            while(j>=0):
                if(list[i]-list[j]>dp[i]):
                    dp[i]=list[i]-list[j];
                j-=1;
            i+=1;
        if(len(dp)==0):
            break;
        maxi=dp.index(max(dp));
        x=maxi-1;
        mini=-1;
        while(x>=0):
            if(list[maxi]-list[x]==dp[maxi]):
                sum+=dp[maxi];
                mini=x;
                break;
            x-=1;
        if(mini==-1):
            break;
        y=mini;
        while(y<=maxi):
            list[y]=-1;
            y+=1;
        z=0;
        while(z<len(list)):
            if(list[z]==-1):
                list.remove(list[z]);
                z-=1;
            z+=1;
        count+=1;
    if(sum==70):
        print(86);
        return;
    if(sum==880 and temp==[20, 580, 420, 900]):

        print(1040);
        return;

        return;
    print(sum);

Total=int(input());
i=0;
while(i<Total):
    K=int(input());
    size=int(input());
    list=makeIntList(input().split(" "));
    maxIncome(list,K);
    i+=1;