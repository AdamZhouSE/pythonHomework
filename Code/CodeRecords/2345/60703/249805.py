n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    numList =[int(x) for x in input().split()];
    flag=0;
    for i in range(0,N):
        if(numList[i]!=i+1):
            ans.append(str(numList[i])+" "+str(i+1));
            flag = 1;
            break;
    if(flag==0):
        ans.append("0 0");

for i in ans:
    print(i);