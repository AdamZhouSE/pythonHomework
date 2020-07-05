def SaD(list):
    sumS=0;
    sumD=0;
    count=0;
    while(len(list)!=0):
        if(int(list[0])>int(list[len(list)-1])):
            if(count%2==0):
                sumS+=int(list[0]);
            else:
                sumD+=int(list[0]);
            list.remove(list[0]);
        else:
            if(count%2==0):
                sumS+=int(list[len(list)-1]);
            else:
                sumD+=int(list[len(list)-1]);
            list.remove(list[len(list)-1]);
        count+=1;
    print(str(sumS)+" "+str(sumD));


Total=int(input());
# i=0;
# list=[];
# while(i<Total):
#     temp=str(input());
#     list.append(temp);
#     i+=1;
list=str(input());
list=list.split(" ");
SaD(list);