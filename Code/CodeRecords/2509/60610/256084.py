length=input();
l=list(map(int,input().split()));
Znum=int(input());
for i in range(Znum):
    string=input();
    ins=string.split()[0];
    if ins=="add":
        l.append(int(string.split()[1]));
    else :
        if(len(l)%2==0):
            a=int(len(l)/2);
        else:
            a=int(len(l)/2)+1;
        print(sorted(l)[a-1]);
        