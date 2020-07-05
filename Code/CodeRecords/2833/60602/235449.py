def Jiafaer(sum,list):
    first=int(max(list));
    list.remove(max(list));
    second=int(max(list));
    if(first+second>=sum):
        print("YES");
    else:
        print("NO");

Total=int(input());
sum=0;
i=0;
list=[];
# while(i<Total):
#
#     i+=1;
listSum=str(input());
listSum=listSum.split(" ");
for element in listSum:
    sum+=int(element);
list=str(input());
list=list.split(" ");
for element in list:
    element=int(element);
Jiafaer(sum,list);