string=input()
string=string.replace("[","");
string=string.replace('"',"");
string=string.split("], ");
for i in range(len(string)):
    if("]" in string[i]):
        string[i]=string[i].replace("]","")
    string[i]=string[i].split(", ")
for i in range(len(string)-1):
    for j in range(i+1,len(string)):
        list=string[j];
        for k in range(1,len(list)):
            if(list[k] in string[i]):
                for l in range(1,len(list)):
                    if(list[l] not in string[i]):
                        string[i]=string[i]+[list[l]];
                string[j]="";
while("" in string):
    string.remove("");
print(string)
