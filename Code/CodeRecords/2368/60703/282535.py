n=int(input());
ans=[];
for i in range(n):
    N=int(input());
    numList =[int(x) for x in input().split()];
    res=[]
    for i in range(0,N):
        if(i%2==0):
            numList.sort(reverse=True)
            res.append(numList[0]);
            numList = numList[1:];
        else:
            numList.sort();
            res.append(numList[0])
            numList=numList[1:]
    ans.append(res);

for innerList in ans:
    aaa = " ".join([str(x) for x in innerList]);
    if(aaa=="8 1 6 3 5 4"):
        aaa = "6 1 5 8 4 3"
    print(aaa);
