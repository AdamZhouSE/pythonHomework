n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    numList = [int(x) for x in input().split()];
    count = 0;
    for i in range(0,N-1):
        for j in range(i+1,N):
            if(numList[i]>numList[j]):
                count+=1;
                ans.append(count);


print(count)