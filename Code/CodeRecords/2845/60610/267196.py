num=int(input());
result=[];
for i in range(num):
    l=list(map(int,input().split()));
    result.append(l);
count=0;
for i in range(len(result)):
    for j in range(len(result)):
        if(result[j][0]<result[i][0])&(result[j][1]>result[i][1]):
            print("Happy Alex");
            count=1;
            break;
    if(count==1):
        break;
if(count==0):
    print("Poor Alex");