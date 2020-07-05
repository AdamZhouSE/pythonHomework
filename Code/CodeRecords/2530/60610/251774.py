string1=input();
string2=input();
result="";
for i in string1:
    while i in string2:
        result=result+i;
        string2=string2.replace(i,"",1);
print(result+string2);