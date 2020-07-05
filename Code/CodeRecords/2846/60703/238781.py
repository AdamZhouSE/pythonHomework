n=int(input());
StrList=input().split();
list=[];
for i in StrList:
    list.append(int(i));
list.sort();
list2=[];
for i in list:
    if((i not in list2) and i!=0):
        list2.append(i);
print(len(list2));