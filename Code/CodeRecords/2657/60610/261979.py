string=input();
N=int(string[0]);
Q=int(string[2]);
sign=[0]*(N+1);
sign[1]=1;
faNode=[0]*(N+1);
for i in range(N-1):
    string=input();
    faNode[int(string[2])]=int(string[0]);
for i in range(Q):
    string=input();
    a = int(string[2])
    if(string[0]=="Q"):
         while(True):
            if(sign[a]==1):
                print(a);
                break;
            else:
                if(sign[faNode[a]]==1):
                    print(faNode[a]);
                    break;
                else:
                    a=faNode[a];
    else:
        sign[a]=1;