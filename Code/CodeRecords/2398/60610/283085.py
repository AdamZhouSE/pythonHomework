num=input().split();
mid=[];
for i in range(int(num[0])):
    mid.append(int(input()))
k=1;
add=sum(mid)+1;
while(add-1>int(num[1])):
    k+=1;
    result=[];
    add=0;
    for i in range(k):
        result.append(mid[i]);
    j=k;
    cout=0;
    cout1=0;
    while(cout!=1):
        if(j!=int(num[0])):
            while (0 in result):
                a = result.index(0);
                result[a] = mid[j];
                j += 1
                if (j == int(num[0])):
                    break;
        if (j == int(num[0])):
            cout1 = result.count(0) + cout1;
            if (cout1 == k):
                cout = 1;
        result=[result[i]-1 for i in range(len(result)) if result[i]!=0];
        add+=1;

print(k)