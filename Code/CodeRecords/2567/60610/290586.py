string=input();
string=string.replace("[","");
string=string.replace("]","");
num=list(map(int,string.split(",")));
low=int(input());
up=int(input())
result=0;
for i in range(len(num)):
    for j in range(len(num)-i):
        if(low<=sum(num[j:j+i+1])<=up):
            result+=1;
print(result)