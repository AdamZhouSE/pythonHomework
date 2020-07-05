string=eval(input());
result=[string[0]];
string.remove(string[0]);
output=0;
while(string!=[]):
    count=0;
    for i in string:
        cout=0;
        for j in result:
            if(i[0]==j[0])|(i[1]==j[1]):
                result.append(i);
                string.remove(i);
                break;
            else:
                cout+=1;
        if(cout==len(result)):
            count+=1;
    if(count==len(string)):
        if(len(result)>output):
            output=len(result);
        if(string!=[]):
            result=[string[0]];
            string.remove(string[0]);
if(len(result)>output):
    output=len(result);
print(output-1);