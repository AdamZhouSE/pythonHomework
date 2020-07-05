num=int(input());
string=input();
l=list(map(int,string.split()));
sum=0;
while(l!=[]):
    result=[];
    for i in l:
        result.append(i*l.count(i));
    sum=max(result)+sum;
    a=result.index(max(result));
    b=l[a];
    while(b in l) | (b-1 in l) |(b+1 in l):
        if(b in l):
            l.remove(b);
        elif(b-1 in l):
            l.remove(b-1);
        else:
            l.remove(b+1);
print(sum)