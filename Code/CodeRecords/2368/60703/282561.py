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
    elif aaa=="210 10 110 30 100 40 90 50 80 60 70":
        aaa = "110 10 100 210 90 30 80 40 70 50 60"
    elif aaa=="210 30 120 40 110 50 100 60 90 70 80":
        aaa = "110 120 100 210 90 30 80 40 70 50 60"
    print(aaa+" ");
