rowstr=input();
rowlist=rowstr.split(" ");
n=int(rowlist[0]);
num=int(rowlist[1]);
list=[-1]*n;
i=0;
result=-1;
while i<num:

    temp=int(input());
    index=temp%n;
    if(list[index]==-1):
        list[index]=temp;
    else:
        result=i+1;
        break;
    i = i + 1;
print(result);
