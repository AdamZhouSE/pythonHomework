k=int(input());
for i in range(0,k):
    n = int(input());
    StrList = input().split();
    NumList = [];
    for i in StrList:
        NumList.append(int(i));
    NumList.sort();
    for i in range(0,n):
        if(len(NumList)-i<=NumList[i]):
            print(len(NumList)-i);
            break;