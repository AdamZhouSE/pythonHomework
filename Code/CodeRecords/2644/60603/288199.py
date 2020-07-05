string=input()[1:-1]
list=string.split(",")
for i in range(len(list)):
    list[i]=int(list[i])
k=int(input())
len=len(list)
sum=0
begin=0
res=-1
sig=0
for i in range(len):
    if (list[i] >= k) :
        sig=1
        ans=1
        break
    sum += list[i];
    if (sum < 1):
        sum = 0;
        begin = i + 1;
        continue;
    j=i-1
    while(list[j+1]<0):
        list[j]=list[j+1]+list[j]
        list[j+1]=0
        j-=1


    if (sum >= k) :
        while ((sum - list[begin] >= k) | (list[begin] <= 0)):
            sum -= list[begin ];
            begin+=1

        length = i - begin + 1;
        if ((res < 0) | (res > length)):
            res = length;
if(sig==1):
    print(1)
else:
    if(res==0):
        print(-1)
    else:print(res)