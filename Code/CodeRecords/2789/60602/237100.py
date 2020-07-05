def squareRoof(list):
    count=0;
    for element in list:
        element=int(element);
    while(True):
        # for element in list:
        #     element=int(element)-1;
        #     if(element==0):
        #         list.remove(element);
        i=0;
        while(i<len(list)):
            list[i]=int(list[i])-1;
            if(list[i]==-1):
                list.remove(list[i]);
                i-=1;
            i+=1;
        if(len(list)>count):
            count+=1;
        else:
            break;
    return count;

Total=int(input());
sum=0;
i=0;
list=[];
ans=[];
while(i<Total):
    sumup=int(input());
    temp = str(input());
    list=temp.split(" ");
    ans.append(squareRoof(list));
    i+=1;
for element in ans:
    print(element);