string1=input().split(",")[::-1];
string2=input().split(",")[::-1];
a1=0;
a2=0;
for i in range(len(string1)):
    if(string1[i]=="1"):
        a1+=pow(-2,i);
for i in range(len(string2)):
    if(string2[i]=="1"):
        a2+=pow(-2,i);
num=a1+a2;
string=""
while(num!=0):
    a=abs(num%(-2));
    if(a==1):
        string=string+"1";
    else:
        string=string+"0";
    num=(num-a)//(-2)
print(list(map(int,string[::-1])))