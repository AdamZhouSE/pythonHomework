string=input();
Pnum=int(string.split()[0]);
Znum=int(string.split()[1]);
result=[0]*Pnum;
for i in range(Znum):
    a=int(input());
    if(result[a-1]==0):
        result[a-1]=1;
    else:
        result[a-1]=0;
    mid=1;
    count=1;
    for i in range(1,len(result)):
        if result[i]!=result[i-1]:
            mid+=1;
        else:
            if mid>count:
                count=mid;
            mid=1;
    if mid > count:
        count = mid;
    mid=1;
    print(count)