num=input();
for i in range(0,num):
    string=raw_input();
    Blist=string.split();
    A=int(Blist[0],2);
    B=int(Blist[1],2);
    print(A*B);