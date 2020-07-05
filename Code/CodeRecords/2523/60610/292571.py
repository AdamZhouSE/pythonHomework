string=input();
row=string.count("],")+1
string=string.replace("[","");
string=string.replace("]","");
string=list(map(int,string.split(",")));
string=sorted(string);
com=len(string)//row
result=[[] for i in range(row)];
i=0;
j=0;
while(i<len(string)):
    if(j%2!=0):
        l=j//2;
        for k in range(com-l):
            result[l].append(string[i]);
            i+=1;
    else:
        l=j//2;
        for k in range(row-l-1):
            result[l+k+1].append(string[i]);
            i+=1;
    j+=1
print(result)