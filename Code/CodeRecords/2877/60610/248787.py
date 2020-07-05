num=input();
string=input();
l=list(map(int,string.split()));
l.sort(key=None,reverse=False);
result=0;
C=0;
count=0;
for i in l:
    if i>=0:
        result=result+i;
    else:
        C=C+i;
        count+=1;
if(C<0):
    if(count==len(l)):
        print(2*l[-1]-C);
    else:
        print(result-C);
else:
    print(result);