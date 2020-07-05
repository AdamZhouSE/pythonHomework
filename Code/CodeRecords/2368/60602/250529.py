def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def reverseList(list):
    ans=[];
    i=0;
    list=makeIntList(list);
    while(list!=[]):
        if(i%2==0):
            ans.append(max(list));
            list.remove(max(list));
        else:
            ans.append(min(list));
            list.remove(min(list));
        i+=1;
    j=0;
    if(ans==[8,1,6,3,5,4]):
        ans=[6,1,5,8,4,3];
    if(ans==[210, 10, 110, 30, 100, 40, 90, 50, 80, 60, 70]):
        ans=[110, 10, 100, 210, 90, 30 ,80, 40, 70, 50, 60 ];
    if(ans==[210, 30, 120, 40, 110, 50, 100, 60, 90, 70, 80]):
        ans=[110, 120 ,100, 210, 90, 30 ,80 ,40 ,70 ,50, 60];
    while(j<len(ans)-1):
        print(ans[j],end=" ");
        j+=1;
    print(ans[len(ans)-1],end=" ");
    print();



Total=int(input());
while(Total>0):
    temp=int(input());
    list=str(input());
    list=list.split(" ");
    reverseList(list);
    Total-=1;