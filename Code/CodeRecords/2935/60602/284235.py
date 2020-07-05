def QAQ(string):
    i=0;
    count=0;
    while(i<len(string)):
        if(string[i]=="Q"):
            j=i+1;
            while(j<len(string)):
                if(string[j]=="A"):
                    t=j+1;
                    while(t<len(string)):
                        if(string[t]=="Q"):
                            count+=1;
                        t+=1;
                j+=1;
        i+=1;
    print(count,end="");

string=input();
QAQ(string);