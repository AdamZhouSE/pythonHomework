nums=[4,8,15,16,23,42]
n=(int)(input())
arr=list(map(int,input().split(' ')))
count=0
group=0
record=[]
while(True):
    judge=False
    temp=[]
    for i in range(len(arr)):
        if(nums.index(arr[i])==count):
            record.append(i)
            count+=1
        if(count==len(nums)):
            judge=True
            break
    if(judge):
        group+=1
        for i in range(len(arr)):
            if(i not in record):
                temp.append(arr[i])
        arr=temp
        record=[]
        count=0
    else:
        break
print(n-6*group)


