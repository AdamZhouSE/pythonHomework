def PoorBabu(string):
    i=0;
    actual=int(string);
    while(i<len(string)):
        if(string[i]=="6"):
            if(len(string)>1):
                string=string[0:i]+"9"+string[i+1:];
            else:
                string="9";
        i+=1;
    print(int(string)-actual);
Total=int(input());
i=0;
while(i<Total):
    temp=input();
    PoorBabu(temp);
    i+=1;
