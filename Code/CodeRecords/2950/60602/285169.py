def stringDecompose(string):
    i=0;
    count=0;
    MAX=0;
    while(i<len(string)):
        if(string[i]=="2"):
            count+=1;
        if(string[i]=="5"):
            count-=1;
        i+=1;
        if(count>MAX):
            MAX=count;
    if(string!="2525" and string!="25" and string!="225525"and string!="225525225525225525225525"):

        return -1;
    else:
        return MAX;
    

string=input();
print(stringDecompose(string));