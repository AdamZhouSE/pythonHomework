num=input().split();
p1=int(num[0])
p2=int(num[1])
p3=int(num[2])
string=input()
i=0;
while(i<=len(string)-1):
    if(string[i]=="-"):
        if(('a'<=string[i-1]<='z')&('a'<=string[i+1]<='z')) |(('0'<=string[i-1]<='9')&('0'<=string[i+1]<='9')):
            string1="";
            for j in range(ord(string[i-1])+1,ord(string[i+1])):
                if(p1==1):
                    string1=string1+chr(j)*p2;
                elif(p1==2):
                    if(('a'<=string[i-1]<='z')):
                        string1 = string1+ chr(j-32) * p2;
                    else:
                        string1 = string1 + chr(j) * p2;
                else:
                    string1 = string1 + "*" * p2;
            if(p3==2):
                string1 = string1[::-1];
            string1 = string[i - 1]+string1+string[i+1];
            string = string.replace(string[i - 1:i + 2], string1, 1)
    i+=1;
print(string)