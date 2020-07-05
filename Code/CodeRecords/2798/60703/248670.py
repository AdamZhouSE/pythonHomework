def getSum(list):
    sun = 0;
    for i in list:
        sun+=i;
    return  sun;


n = int(input());
numList =  [int(x) for x in input().split()];
sumAll = getSum(numList);
average = int(sumAll/3);
if(average*3!=sumAll):
    print(str(0));
else:
    all = 0;
    for i in range(0,len(numList)):
        if(getSum(numList[0:i+1])==average):
            for j in range(i+1,len(numList)):#越界隐患
                if(getSum(numList[i+1:j+1])==average):
                    all+=1;
    print(all);