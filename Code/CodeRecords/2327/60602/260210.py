def DImatch(string):
    num=len(string)+1;
    list=[];
    ans=[];
    i=0;
    while(i<num):
        list.append(i);
        i+=1;

    j=0;
    while(j<len(string)):
        if(string[j]=="I"):
            ans.append(list[0]);
            list.remove(list[0]);
        else:
            ans.append(list[len(list)-1]);
            list.remove(list[len(list)-1]);
        j+=1;
    ans.append(list[0]);
    print(ans);

list=str(input());
DImatch(list);