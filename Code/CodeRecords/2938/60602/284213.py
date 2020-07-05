def dicSort():
    i=1;
    list=[];
    while(i<=100):
        list.append(str(i));
        i+=1;
    list=sorted(list);
    i=0;
    while(i<len(list)):
        print(list[i]);
        i+=1;

dicSort()