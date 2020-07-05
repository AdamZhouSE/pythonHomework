num=int(input());
buliding=[];

for i in range(num):
    string=input();
    l=list(map(int,string.split()));
    buliding.append(l);
buliding.sort(key=None,reverse=False);
for i in range(len(buliding)):
    j=i+1;
    while(j<len(buliding)):
        if buliding[j][0]>=buliding[i][1]:
            j+=1;
        elif (buliding[j][0]<buliding[i][1]) & (buliding[j][1]>buliding[i][1]):
            if buliding[j][2]>=buliding[i][2]:
                buliding[i][1]=buliding[j][0];
            else:
                buliding[j][0] = buliding[i][1];
            j+=1;
        else:
            if(buliding[j][2]<=buliding[i][2]):
                buliding.remove(buliding[j]);
            else:
                buliding.append([buliding[i][0],buliding[j][0]],buliding[i][2]);
                buliding.append([buliding[j][1],buliding[i][1],buliding[i][2]]);
                buliding.remove(buliding[i]);
                buliding.sort(key=None,reverse=False);
                j+=1;
sum=0;
for i in buliding:
    sum=sum+(i[1]-i[0])*i[2];
print(sum);