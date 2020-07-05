def findDifference(string):
    i=0;
    count=0;
    model="CODEFESTIVAL2016";
    while(i<len(string)):
        if(string[i]!=model[i]):
            count+=1;
        i+=1;
    print(count);

string=input();
findDifference(string);