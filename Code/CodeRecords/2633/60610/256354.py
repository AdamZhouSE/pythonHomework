string=input();
num=int(string.split()[0]);
ins=int(string.split()[1]);
con=list(map(int, input().split()));
for i in range(ins):
    string=input();
    l = list(map(int,string.split()));
    if(l[0]==1):
        L=l[1];
        R=l[2];
        K=l[3];
        D=l[4];
        for i in range(R-L+2):
            con[L+i-1]=con[L+i-1]+K+D*i;
    else:
        print(con[l[1]-1]);