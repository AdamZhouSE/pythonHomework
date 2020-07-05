string=input();
while string[len(string)-1]=="1":
    string=string.rstrip("1");
count=1;
for i in range(0,len(string)-1):
    if(string[i]!=string[i+1]):
        count+=1;
print(count,end="");
