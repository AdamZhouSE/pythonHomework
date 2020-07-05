size=int(input());
i=0;
list=[];
while(i<size):
    list.append(int(input()));
    i+=1;

if(len(list)==1):
    print(0);
    exit(0);

count=0;
while(len(list)>1):
    temp = max(list[0], list[1]);
    tempi = 0;
    i = 0;
    while(i<len(list)-1):
        if(max(list[i],list[i+1])<temp):
            temp=max(list[i],list[i+1]);
            if(list[i]>list[i+1]):
                tempi=i+1;
            else:
                tempi=i;
        i+=1;
    count+=temp;
    list=list[0:tempi]+list[tempi+1:];

print(count);