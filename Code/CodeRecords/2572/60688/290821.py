reqlist = input().split(" ");
reqlist = list(int(x) for x in reqlist);
L=reqlist[0];
ls=[1 for i in range(L+1)];
T=reqlist[1];
Ts=[i for i in range(L+1)];
reqs=reqlist[2];
for i in range(reqs):
    tempreq = input().split(" ");
    if tempreq[0]=="C":
        l=int(tempreq[1]);
        r=int(tempreq[2])+1;
        color = int(tempreq[3]);
        for j in range(l,r):
            ls[j]=color;
    if tempreq[0]=="P":
        l = int(tempreq[1]);
        r = int(tempreq[2]) + 1;
        result=len(set(ls[l:r]))
        print(result)