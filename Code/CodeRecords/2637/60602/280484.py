def mountainList(list):
    i=0;
    while(i<len(list)-1):
        if(list[i+1]<list[i]):
            print(i);
            return
        i+=1;

list=eval(input());
mountainList(list);