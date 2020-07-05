num=input();
for j in range(0,num):
    str=raw_input();
    patt=raw_input();
    a=0;
    for i in str:
        if i in patt:
            print(i);
            a=1;
            break;
    if(a==0):
        print("$");