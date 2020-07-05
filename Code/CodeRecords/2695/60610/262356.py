def DIgui(sonNode,a,value,num):
    value[a - 1] += num;
    if(sonNode[a]!=[]):
        for i in sonNode[a]:
            DIgui(sonNode,i,value,num);

string=input();
N=int(string[0]);
M=int(string[2]);
sonNode=[[]]*(N+1);
value=list(map(int,input().split()));
faNode=[0]*(N+1);

for i in range(N-1):
    c=[];
    string=input();
    c.extend(sonNode[int(string[0])]);
    c.append(int(string[2]));
    sonNode[int(string[0])]=c;
    faNode[int(string[2])]=int(string[0]);
for i in range(M):
    string=input();
    a=int(string[2]);
    if(string[0]=="1"):
        value[a-1]=value[a-1]+int(string[4]);
    elif(string[0]=="2"):

        DIgui(sonNode,a,value,int(string[4]));
    else:
        sum=value[a-1];
        while(faNode[a]!=0):
            a = faNode[a];
            sum=sum+value[a-1];
        print(sum)
