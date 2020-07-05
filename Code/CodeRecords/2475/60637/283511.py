tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    arr=list(map(int,input().split(' ')))
    list.sort(arr)
    record=1
    i=0
    temp=1
    while(i<n-1):
        if(arr[i+1]==arr[i]+1):
            temp+=1
        else:
            if(temp>record):
                record=temp
            temp=1
        i+=1
    print(record)
