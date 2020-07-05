num=int(input());
count=0;
for i in range(2,num+1):
    cout=0;
    for j in range(2,int(pow(i,0.5))+1):
        if(i%j==0):
            cout=1;
            break;
    if(cout==0):
        count+=1;
result=1;
for i in range(1,count+1):
    result=result*i;
for i in range(1,num-count+1):
    result=result*i;
result=result%(1000000007)
print(result)