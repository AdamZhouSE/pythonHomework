num=int(input());
envelops=[];
for i in range(num):
    envelops.append(list(map(int,input().split(","))));
envelops=sorted(envelops);
count=0;
result=0;
for j in range(len(envelops)):
    current=envelops[j];
    for i in range(j,len(envelops)):
        if((envelops[i][0]>current[0])&(envelops[i][1]>current[1])):
            count+=1;
            current=envelops[i];
    if(count>result):
        result=count;
    count=0;
print(result+1)