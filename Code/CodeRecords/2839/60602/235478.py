def nameList(list):
    i=0;
    j=0;
    judge=False;
    while(i<len(list)):
        while(j<i):
            if(list[j]==list[i]):
                print("YES");
                judge=True;
                break;
            j+=1;
        j=0;
        if(not judge):
            print("NO");
        judge=False;
        i+=1;

Total=int(input());
sum=0;
i=0;
list=[];
while(i<Total):
    temp = str(input());
    list.append(temp);
    i+=1;
# listSum=str(input());
# listSum=listSum.split(" ");
# for element in listSum:
#     sum+=int(element);
nameList(list);