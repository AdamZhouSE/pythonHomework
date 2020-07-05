n=int(input());
listHOUR=[];
listMIN=[];
for i in range(0,n):
    a,b=map(int,input().split());
    listHOUR.append(a);
    listMIN.append(b);
max=0;
list=[];
for i in range(0,n):
    list.append(0);

for i in range(0,n):
    for j in range(0,n):
        if((listMIN[j]==listMIN[i])and(listHOUR[j]==listHOUR[i])):
            list[i]+=1;
list.sort(reverse=True);
print(list[0]);