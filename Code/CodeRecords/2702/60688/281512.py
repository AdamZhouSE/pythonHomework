numberlist1=list(input());
numberlist1=list(int(i)for i in numberlist1);
cons=len(numberlist1);
result=[];
result.append(numberlist1);

print();
while(numberlist1 = list(input())):
    numberlist1 = list(int(i) for i in numberlist1);
    result.append(numberlist1);
print(numberlist1)
9
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