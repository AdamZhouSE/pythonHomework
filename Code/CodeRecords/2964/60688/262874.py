def countTheDiffStr(a,b):
    lie=len(a)+1;
    hang=len(b)+1;
    dp=[];
    for i in range(lie):
        dp.append([0]*hang)
    for i in range(lie):
        dp[i][0]=i;
    for i in range(hang):
        dp[0][i]=i;
    for i in range(1,lie):
        for j in range(1,hang):
            if (a[i-1]==b[j-1]):
                dp[i][j]=dp[i-1][j-1];
            else:
                temp=dp[i-1][j-1]+1;
                min1=min(dp[i-1][j]+1,dp[i][j-1]+1);
                dp[i][j]=min(temp,min1);

    return dp[lie-1][hang-1]

nums=int(input())
strlists=[];
for i in range(nums):
    strlists.append(input());
result=[];
for i in range(0,len(strlists)-1):
    for j in range(i, len(strlists)):
        result.append(countTheDiffStr(strlists[i],strlists[j]))
resultnumlist=[0]*9;
for i in result:
    if i<=8 :
        resultnumlist[i]+=1
resultnumlist=list(str(x) for x in resultnumlist)
resultstr=" ".join(resultnumlist[1:])
print(resultstr，end="")