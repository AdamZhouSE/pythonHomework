list=[];
Str=input();
Str=str(Str);
for i in range(0,len(Str)):
    list.append(Str[i:len(Str)]);
list.sort();
#print(list);
for i in  range(0,len(Str)-1):
    print(len(Str)-len(list[i])+1,end=" ");
print(len(Str)-len(list[len(Str)-1])+1);
