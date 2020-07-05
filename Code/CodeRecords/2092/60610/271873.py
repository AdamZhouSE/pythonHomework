num=int(input());
result=[[i] for i in range(1,num+1)];
l=list(map(int,input().split()));
con=0;
count=1;
mid=[[] for i in range(num)];
while(True):
    for i in range(len(l)):
        mid[l[i]-1]=result[i]+mid[l[i]-1];
    result=mid;
    for i in range(len(result)):
        if result[i].count(i+1)==1:
            con=1;
    if con==1:
        break;
    count+=1;
    mid=[[] for i in range(num)];
print(count,end="")
