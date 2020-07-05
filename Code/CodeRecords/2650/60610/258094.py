string=input();
num=int(string.split()[0]);
ins=int(string.split()[1]);
con=list(map(int, input().split()));
for i in range(ins):
    string=input();
    l = list(map(int,string.split()));
    L = l[0];
    R = l[1];
    result=con[L-1:R];
    result.sort(key=None,reverse=False);
    print(result[l[2]-1]);