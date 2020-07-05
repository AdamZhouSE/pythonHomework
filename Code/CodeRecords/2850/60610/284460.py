num=int(input());
string=input();
mid=list(map(int,string.split()));
result=mid.count(1);
for k in range(1,num+1):
    for i in range(num):
        for j in range(i,i+k):
            if(j>=num):
                break;
            mid[j]=1-mid[j];
        if(mid.count(1)>result):
            result=mid.count(1);
        mid = list(map(int, string.split()));
print(result)