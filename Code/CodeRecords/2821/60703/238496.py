n=int(input());
list=input().split(" ");
list2=[];
for i in list:
    list2.append(int(i));
num1=0;
num2=0;
turn=0;
for i in range(0,n):
    if(list2[0]>=list2[len(list2)-1]):
        temp=list2[0];
        list2=list2[1:];
    else:
        temp=list2[len(list2)-1];
        list2=list2[:len(list2)-1];
    if(turn==0):
        num1=num1+temp;
        turn=1;
    else:
        num2=num2+temp;
        turn=0;
Str=str(num1)+" "+str(num2);
print(Str);