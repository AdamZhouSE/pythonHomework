string=input();
string=string.replace("[","");
string=string.replace("]","");
string=string.replace('"',"");
string=string.split(",");

result=[];

while(string!=[]):
    count=1;
    mid=[string[0]];
    string.remove(string[0]);
    while(count!=0):
        output=0;
        i=0;
        while(i<len(string)):
            cout=0;
            for j in mid:
                first=[];
                if(len(string[i])==len(j)):
                    for k in range(len(j)):
                        if(string[i][k]!=j[k]):
                            first.append(k);
                            if(len(first)>2):
                                break;
                    if(len(first)==2):
                        if(j[first[0]]==string[i][first[1]])&(j[first[1]]==string[i][first[0]]):
                            mid.append(string[i]);
                            string.remove(string[i]);

                            break;
                        else:
                            cout+=1;

                    else:
                        cout+=1;
            if(cout==len(mid)):
                i+=1;
                output+=1;
        if(output==len(string)):
            count=0;

    result.append(mid);
print(len(result))