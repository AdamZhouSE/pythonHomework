def GPAcalcu(string):
    count=0;
    i=0;
    while(i<len(string)):
        if(string[i]=="A"):
            count+=4;
        elif(string[i]=="B"):
            count+=3;
        elif(string[i]=="C"):
            count+=2;
        elif(string[i]=="D"):
            count+=1;
        i+=1;
    if(count/len(string)==0.0):
        print(0,end="");
    else:
        print(format(count/len(string),'.14f'),end="");

Total=input();
string=input();
GPAcalcu(string);