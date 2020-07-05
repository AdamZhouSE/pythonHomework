num=int(input());
string=input().split();
i=len(string)
count=0;
result=0;
while(i>0):
    for j in range(len(string)-i+1):
        mid=string[j:j+i];
        if(mid.count("2")==i//2)&(mid.count("1")==i//2):
            a=len(mid)//2;
            if(mid[:a].count("1")==a)|(mid[:a].count("2")==a):
                result=i;
                count=1;
                break;
    if(count==1):
        break;
    i-=1;
print(result);