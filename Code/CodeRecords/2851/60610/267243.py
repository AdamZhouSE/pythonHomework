num=int(input());
mid=[];
for i in range(num):
    l=list(map(int,input().split()));
    sum=l[0]+l[1];
    mid.append(sum);
count=0;
result=-1;
while(count!=len(mid)):
    count = 0;
    result += 1;
    for i in mid:
        if(i<=result):
            count+=1;
print(result)
