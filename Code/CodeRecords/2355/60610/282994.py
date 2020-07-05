num=input().split();
keys=list(map(int,input().split()));
mid=[];
for i in range(int(num[1])):
    mid.append(list(map(int,input().split())));
result=10000;
output=0;
for i in mid:
    left=[i[0]];
    right=[i[1]];
    count=0;
    j=0;
    while(count!=int(num[1])-1):
        if mid[j]==i:
            j+=1
        else:
            if((mid[j][0] in left) | (mid[j][1] in left)):
                if(mid[j][0] not in left):
                    left.append(mid[j][0]);
                    count+=1;
                elif(mid[j][1] not in left):
                    left.append(mid[j][1]);
                    count+=1;
            elif ((mid[j][0] in right) | (mid[j][1] in right)):
                if (mid[j][0] not in right):
                    right.append(mid[j][0]);
                    count += 1;
                elif (mid[j][1] not in right):
                    right.append(mid[j][1]);
                    count += 1;
            j+=1;
        j=j%(int(num[1]))
    sumleft=0;
    sumright=0;
    for k in left:
        sumleft=sumleft+keys[k-1];
    for k in right:
        sumright=sumright+keys[k-1];
    if(abs(sumright-sumleft)<result):
        result=abs(sumright-sumleft);
print("Case 1: %d"%result)