n = int(input());
list1 = [int(x) for x in input().split()];
list2 = [int(x) for x in input().split()];
k1=list1[0];
k2=list2[0];
list1=list1[1:];
list2=list2[1:];
index  =0;
while(len(list2)!=0 and len(list1)!=0 and index<=3*n):
    index+=1;
    if(list1[0]>list2[0]):
        a=list1[0];
        b=list2[0];
        list1=list1[1:];
        list2=list2[1:];
        list1.append(b);
        list1.append(a);
    else:
        a = list1[0];
        b = list2[0];
        list1 = list1[1:];
        list2 = list2[1:];
        list2.append(a);
        list2.append(b);

if(len(list2)!=0 and len(list1)!=0):
    print(-1);
elif(len(list2)!=0):
    print(index,end=" ");
    print(2);
else:
    print(index,end=" ");
    print(1);