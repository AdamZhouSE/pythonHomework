def Tanya(list):
    sum=0;
    count=1;
    ans=[];
    for element in list:
        if(int(element)==1):
            sum+=1;
            ans.append(count);
            count=1;
        else:
            count+=1;
    ans.append(count);
    ans.remove(ans[0]);
    i=0;
    print(sum);
    while(i<len(ans)-1):
        print(ans[0],end=" ");
        i+=1;
    print(ans[len(ans)-1]);


Total=int(input());
list=str(input());
list=list.split(" ");
Tanya(list);