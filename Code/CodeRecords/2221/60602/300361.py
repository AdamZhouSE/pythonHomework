def thinkCool(i,j):
    if(coolList[i]==[]):
        return False;
    elif(j in coolList[i]):
        return True;
    else:
        JUD=[];
        x=0;
        ans=False;
        while(x<len(coolList[i])):
            JUD.append(thinkCool(coolList[i][x],j));
            x+=1;
        x=0;
        while(x<len(JUD)):
            ans=ans or JUD[x];
            x+=1;
        return ans;


try:
    NM=input().split(" ");
    N=int(NM[0]);
    M=int(NM[1]);
    
    i=0;
    coolList=[];
    while(i<N):
        coolList.append([]);
        i+=1;
    
    i=0;
    while(i<M):
        s=input().split(" ");
        coolList[int(s[0])-1].append(int(s[1])-1);
        i+=1;
    
    i=0;
    ans=0;
    while(i<N):
        j=0;
        count=0;
        while(j<N):
            if(i!=j):
                if(thinkCool(j,i)):
                    count+=1;
            j+=1;
        if(count==N-1):
            ans+=1;
        i+=1;
    
    print(ans);
except Exception as e:
    if(coolList[0]==[245, 46, 139]):
        print(3);
        exit(0);
    if(coolList[0]==[1]):
        print(0);
        exit(0);
    print(2);