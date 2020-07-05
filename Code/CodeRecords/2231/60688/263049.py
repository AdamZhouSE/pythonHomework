nums=int(input());
judge=[];
for i in range(nums):
    result = [];
    n=int(input());
    for i in range(2,n+1):
        while(n%i==0):
            result.append(i)
            n/=i;
    if(len(result)==3):judge.append(1);
    else:judge.append(0);
for i in judge:
    print(i)