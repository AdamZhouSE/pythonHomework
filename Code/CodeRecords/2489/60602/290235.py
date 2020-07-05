def calcuListSum(list,lower,upper):
    i=0;
    count=0;
    while(i<len(list)):
        j=i+1;
        while(j<=len(list)):
            if(sum(list[i:j])>=lower and sum(list[i:j])<=upper):
                count+=1;
            j+=1;
        i+=1;
    print(count);

list=eval(input());
lower=int(input());
upper=int(input());

calcuListSum(list,lower,upper);