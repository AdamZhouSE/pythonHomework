num=int(input());
mid=[0 for i in range(num+1)];
for i in range(1,num+1):
    mid[i]=(int(input()));
result=0;
for i in range(1,num+1):
    j=i;
    count=0;
    while(mid[j]!=-1):
        j=mid[j];
        count+=1;
    if(count>result):
        result=count;
print(result+1)