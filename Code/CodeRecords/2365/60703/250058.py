n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    numList =[int(x) for x in input().split()];
    for i in range(0,N-1):
        x = int(str(numList[0])+str(numList[1]));
        y = int(str(numList[1])+str(numList[0]));
        if(x>y):
            numList[1] =x;
        else:
            numList[1] = y;
        numList = numList[1:];
    ans.append(str(numList[0]));

for i in ans:
    print(i);