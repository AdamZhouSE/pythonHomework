n=(int)(input())
arr=list(map(int,input().split(' ')))
sum=0
record=-1
for i in range(n):
    if(arr[i]==1 and record!=1):
        record=1
    elif(arr[i]==2 and record!=0):
        record=0
    elif(arr[i]==3):
        if(record>=0):
            record=1-record
        else:
            count=0
            judge=False
            activity=-1
            for j in range(i,n):
                if(arr[j]==3):
                    count+=1
                elif(arr[j]==0):
                    break
                else:
                    activity=0 if arr[j]==2 else 1
                    judge=True
                    break
            if(not judge):
                record=0
            else:
                record=activity if count%2==0 else 1-activity

    else:
        sum+=1
        record=-1
print(sum)


