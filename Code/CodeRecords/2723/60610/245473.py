num=input();
for i in range(num):
    string=raw_input();
    numList=list(string);
    while len(numList)!=1:
        result=0;
        for i in numList:
            result=int(i)+result;
        string=str(result);
        numList=list(string);
    print("".join(numList));