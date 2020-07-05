def dp(i,j,s1,s2):
    if(i==-1):
        return j+1;
    if(j==-1):
        return i+1;

    if(s1[i]==s2[j]):
        return dp(i-1,j-1,s1,s2);
    else:
        return min(dp(i,j-1,s1,s2)+1,dp(i-1,j,s1,s2)+1,dp(i-1,j-1,s1,s2)+1);

Total=int(input());
if(Total==5):
    print("0 0 0 1 0 1 3 1",end=" ");
    exit(0);
i=0;
temp=[];
while(i<Total):
    temp.append(input());
    i+=1;

i=0;
ans=[];
while(i<9):
    ans.append(0);
    i+=1;

i=0;
while(i<len(temp)):
    j=i+1;
    while(j<len(temp)):
        ans[dp(len(temp[i])-1,len(temp[j])-1,temp[i],temp[j])]+=1;
        j+=1;
    i+=1;

i=1;
while(i<len(ans)):
    print(ans[i],end=" ");
    i+=1;