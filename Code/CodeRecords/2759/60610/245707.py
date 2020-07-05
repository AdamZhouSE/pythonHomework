num=input();
for i in range(num):
    string=raw_input();
    numList=string.split();
    count=0
    for j in range(int(numList[0]),int(numList[1])+1):
        a=int(numList[2]);
        b=int(numList[3]);
        if (j%a==0) | (j%b==0):
            count+=1;
    print(count);