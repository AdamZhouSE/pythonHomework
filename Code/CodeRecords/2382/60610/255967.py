num=int(input());
result=[];
for i in range(num):
    area=list(map(int,input().split()));
    result.append(area);
result.sort(key=None,reverse=False);
while result!=[]:
    b=[];
    a=result[0];
    result.remove(result[0]);
    for i in result:
        if i[0]<=a[1]:
            if i[1]>=a[1]:
                a[1]=i[1];
                b.append(i);
    for i in b:
        result.remove(i);
    print(" ".join(list(map(str,a))));

