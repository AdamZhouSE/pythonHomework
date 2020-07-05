num=int(input());
string=input();
l=list(map(int,string.split()));
sum=0;
while(l!=[]):
    result=[];
    for i in l:
        result.append(i*l.count(i));
    a = result.index(max(result));
    b=l[a];
    if((b-1)*l.count(b-1)+(b+1)*l.count(b+1)>max(result)):
        if((b-2)*l.count(b-2)+(b)*l.count(b)>(b-1)*l.count(b-1)+(b+1)*l.count(b+1))|((b+2)*l.count(b+2)+(b)*l.count(b)>(b-1)*l.count(b-1)+(b+1)*l.count(b+1)):
            sum = max(result) + sum;
            while (b in l) | (b - 1 in l) | (b + 1 in l):
                if (b in l):
                    l.remove(b);
                elif (b - 1 in l):
                    l.remove(b - 1);
                else:
                    l.remove(b + 1);
        else:
            sum=sum+(b-1)*l.count(b-1)+(b+1)*l.count(b+1);
            while (b in l) | (b - 1 in l) | (b + 1 in l)|(b + 2 in l)|(b -2 in l):
                if (b in l):
                    l.remove(b);
                elif (b - 1 in l):
                    l.remove(b - 1);
                elif (b +2 in l):
                    l.remove(b +2);
                elif (b - 2 in l):
                    l.remove(b - 2);
                else:
                    l.remove(b + 1);
    else:
        sum = max(result) + sum;
        while (b in l) | (b - 1 in l) | (b + 1 in l):
            if (b in l):
                l.remove(b);
            elif (b - 1 in l):
                l.remove(b - 1);
            else:
                l.remove(b + 1);
print(sum)
