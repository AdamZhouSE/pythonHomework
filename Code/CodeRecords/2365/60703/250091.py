n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    numList =[int(x) for x in input().split()];
    for i in range(0,N-1):
        for j in range(i+1,N):
            x = int(str(numList[i])+str(numList[j]));
            y = int(str(numList[j])+str(numList[i]));
            if(x<y):
                temp = numList[i];
                numList[i] = numList[j];
                numList[j] = temp;
 #       numList = numList[1:];
    ans.append("".join([str(x) for x in numList]));

for i in ans:
    print(i);