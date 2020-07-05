n,m=map(int,input().split());
Astr = input().split();
Bstr = input().split();
Anum=[];
Bnum=[];
for i in  Astr:
    Anum.append(int(i));
for i in Bstr:
    Bnum.append(int(i));
res=[];
for i in Bnum:
    temp=0;
    for j in Anum:
        if(j<=i):
            temp+=1;
    res.append(temp);
STRresult="";
for j in res:
    STRresult=STRresult+str(j)+" ";
print(STRresult[:len(STRresult)-1]);
