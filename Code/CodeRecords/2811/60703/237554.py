p,n=map(int,input().split(" "));
num=-1;
list=[];
flag=0;
for i in range(0,n):
    number=int(input())%p;
    if(flag==1):
        continue;
    else:
        if(number in list):
            flag=1;
            num= i+1;
        else:
            list.append(number);
print(num);