n=int(input());
listStr=input().split(" ");
list=[];
for i in listStr:
    list.append(int(i));
list.sort();
if(n==2):
    print(0);
else:
    if(list[n-1]-list[1]>=list[n-2]-list[0]):
        print(list[n-2]-list[0]);
    else:
        print(list[n-1]-list[1]);