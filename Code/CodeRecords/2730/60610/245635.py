num=input();
for i in range(num):
    length=input();
    string=raw_input();
    list=string.split();
    result=0;
    for i in list:
        result=result+int(i);
    if(result%3==0):
        print(1);
    else:
        print(0);