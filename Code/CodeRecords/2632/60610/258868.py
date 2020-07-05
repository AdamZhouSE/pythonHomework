string=input();
N=int(string[0]);
M=int(string[2]);
result=[0]*N;
a=[0]*N;
num=0;
for i in range(M):
    string=input();
    if(string[0]=="D"):
        a .append( int(string[2]));
        result[a[-1]-1]=1;
    elif(string[0]=="R"):
        result[a[-1]-1] =0;
        a.remove(a[-1]);
    else:
        b = int(string[2]);
        if(result[b-1]==1):
            print(0)
        else:
            s=0;
            t=0
            s="".join(list(map(str,result[b:]))).find("1");
            t="".join(list(map(str,result[:b-1]))).rfind("1");
            if ((s==-1)&(t!=-1)):
                num=num+len(result)-1-t;
            elif ((s!=-1)&(t==-1)):
                num=num+b+s;
            elif ((s==-1)&(t==-1)):
                num=N
            elif((s!=-1)&(t!=-1)):
                 num=num+b-1-t+s;
            print(num);
            num=0;
