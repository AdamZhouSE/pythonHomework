num=input();
for i in range(num):
    string=raw_input();
    numList=string.split();
    result=pow(int(numList[0]),int(numList[1]))%int(numList[2]);
    print(result);