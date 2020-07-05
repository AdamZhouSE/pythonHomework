def Sumup(num):
    i=1;
    sum=0;
    count=0;
    while(i<=num):
        j=i;
        while(sum<num):
            sum+=j;
            j+=1;
        else:
            if(sum==num):
                count+=1;
        i+=1;
        sum=0;
    print(count);
Target=int(input());
Sumup(Target);