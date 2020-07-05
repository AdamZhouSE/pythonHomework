string=input().split();
num_heap=int(string[0]);
num_ops=int(string[1]);
string=list(map(int,input().split()));
result=[];
mid=string
for i in range(num_heap):
    result.append([string[i]]);

for i in range(num_ops):
    string=list(map(int,input().split()));
    if(string[0]==1):
        a=mid[string[1]-1];
        b=mid[string[2]-1];
        for j in result:
            if(a in j):
                a=result.index(j);
                break;
        for j in result:
            if(b in j):
                b=result.index(j);
                break;

        result[min(a,b)]=result[min(a,b)]+result[max(a,b)];
        result.remove(result[max(a,b)]);
    else:
        a=mid[string[1]-1]
        for i in result:
            if a in i:
                print(min(i));
                i.remove(min(i))



