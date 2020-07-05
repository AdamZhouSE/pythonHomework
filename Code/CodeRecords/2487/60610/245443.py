num=int(input());
for i in range(0,num):
    number=int(input());
    string=input();
    listName=string.split();
    result=[];
    count=0;
    name="";
    for i in listName:
        if i not in result:
            result.append(i);
    for i in result:
        if listName.count(i)>count:
            count=listName.count(i);
            name=i;
        elif listName.count(i)==count:
            if i<name:
                name=i;
    print(name,end=" ");
    print(count);
