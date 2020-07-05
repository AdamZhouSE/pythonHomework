label=int(input());
result=[];
n=0;
place=0;
while(pow(2,n)<=label):
    n+=1;
while(n>0):
    result.append(label);
    if(n%2==0):
        place=((pow(2,n)-label)-1)//2;
        n -= 1;
        label = pow(2, n) - pow(2, n - 1) + place;
    else:
        n-=1;
        place=(label-pow(2,n))//2;
        label=pow(2,n)-place-1;
result=result[::-1];
print(result);