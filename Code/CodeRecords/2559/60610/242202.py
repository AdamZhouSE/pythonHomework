num=input();
for i in range(0, num):
    string=raw_input();
    a=0;
    for j in string:
        num=string.count(j,0,len(string));
        if (num!=1):
            a=1;
    if(a==0):
        print(1);
    else:
        print(0);
    a=0;