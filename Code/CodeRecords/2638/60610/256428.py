string=input();
num=int(string.split()[0]);
ins=int(string.split()[1]);
con=list(map(int, input().split()));
for i in range(ins):
    string=input();
    l = list(map(int,string.split()));
    L = l[1];
    R = l[2];
    if(l[0]==1):
        K=l[3];
        for i in range(L-1,R):
            con[i]=con[i]+K;
    else:
        mid=0;
        for i in range(L-1,R):
            mid=mid+con[i];
        ave=mid/(R-L+1)
        if (l[0]==2):
            print("%.4f"%ave);
        else:
            result=0;
            for i in range(L-1,R):
                result=result+pow(con[i]-ave,2);
            print("%.4f"%(result/(R-L+1)));
