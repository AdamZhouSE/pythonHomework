number=input();
for i in range(0,number):
    start=raw_input();
    l0=start.split();
    num=int(l0[0]);
    L=int(l0[1]);
    R=int(l0[2]);
    string=bin(num).replace("0b","");
    l=list(string);
    for i in range(L,R+1):
        if(l[i]=="0"):
            l[i]="1";
        else:
            l[i]="0";
    string="".join(l);
    result=int(string,2);
    print(result);