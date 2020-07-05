string=input().split();
num=int(string[0]);
time=int(string[1]);
book_time=list(map(int,input().split()));
result=0;
mid=0;
count=0;
for i in range(num):
    for j in range(i,num):
        if(mid+book_time[j]<=time):
            mid=mid+book_time[j];
            count+=1;
        else:
            break;
    if(count>result):
        result=count;
    count=0;
    mid=0;
print(result);
