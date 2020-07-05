num=input();
connections=sorted(input());
result=[connections[0]];
for i in range(1,len(connections)):
    for j in range(len(result)):
        if ((connections[i][0] in result[j])|(connections[i][1] in result[j])):
            if((connections[i][0] not in result[j])):
                result[j]=result[j]+[connections[i][0]];
            elif((connections[i][1] not in result[j])):
                result[j]=result[j]+[connections[i][1]];
        else:
            result.append(connections[i]);
sum=0;
for i in result:
    sum+=len(i);
if(len(connections)<num-1):
    print(-1);
else:
    print(num-sum+len(result)-1)
    