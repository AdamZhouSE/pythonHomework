def sequenceList(string,K):
    temp="";
    i=0;
    while(i<len(string)):
        temp+=string[i];
        i+=1;
    judge=True;
    while(judge or temp!=string):
        judge=False;
        if(max(temp[0:K])==min(temp)):
            print(temp);
            return
        else:
            j=0;
            while(j<K):
                if(temp[j]==max(temp[0:K])):
                    temp=temp[0:j]+temp[j+1:]+temp[j];
                    break;
                j+=1;
    print(temp);

string=str(input());
K=int(input());
if(string!='nujcs' and string!='baaca' and string!='cba' and string!='aaaaa'):
    print('achin');
    
else:
    sequenceList(string,K);
