list=input();
num=len(list)/3;
l=[];
count=1;
for i in range (0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            count=count+1;
            if count>num:
                if list[i] not in l:
                    l.append(list[i]);
    count=1;
print(l);