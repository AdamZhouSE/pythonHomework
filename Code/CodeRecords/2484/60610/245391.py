num=input();
for i in range(0,num):
    length=raw_input();
    stringA=raw_input();
    stringB=raw_input();
    listA=stringA.split();
    listB=stringB.split();
    result=[];

    for j in listA:
        if j not in result:
            result.append(j);
    for j in listB:
        if j not in result:
            result.append(j);
    print(len(result));