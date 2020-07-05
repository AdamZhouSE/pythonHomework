strs=list(input());
ans=[0 for i in range(len(strs))];
depth=0;
for i in range(len(strs)):
    if strs[i]=="(":
        depth+=1;
        if (depth%2==0): ans[i]=1;
    else:
        if(depth%2==0):ans[i]=1;
        depth-=1;
print(ans);