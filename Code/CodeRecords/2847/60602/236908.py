def campLevel(levelYear,Current,Target):
    Sum=0;
    Current=int(Current);
    Target=int(Target);
    Gap=Target-Current;
    Current-=1;
    while(Gap>0):
        Sum+=int(levelYear[Current]);
        Gap-=1;
        Current+=1;
    print(Sum);

Total=int(input());
sum=0;
i=0;
# list=[];
# while(i<Total):
#     temp = str(input());
#     list.append(temp);
#     i+=1;
listSum=str(input());
listSum=listSum.split(" ");
list=str(input());
list=list.split(" ");
# for element in listSum:
#     sum+=int(element);
campLevel(listSum,list[0],list[1]);