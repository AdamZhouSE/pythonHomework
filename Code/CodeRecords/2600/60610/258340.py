string=input();
num=input().split();
destory=list(map(int,(input().split())));
for i in destory:
    num[i-1]=" ";
    count=0;
    sum=0;
    for j in num:
        if(j!=" "):
            count=count+int(j);
        else:
            if count>sum:
                sum=count;
            count=0;
    if count > sum:
        sum = count;
    print(sum);
