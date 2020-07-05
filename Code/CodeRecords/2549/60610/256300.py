string=input();
num=int(string.split()[0]);
ins=int(string.split()[1]);
l=list(map(int,input().split()));
for i in range(ins):
    string=input();
    if string[0]=="2":
        l.append(int(string.split()[1]));
    elif string[0]=="1":
        print(sorted(l,reverse=True)[int(string[2])-1]);
        
