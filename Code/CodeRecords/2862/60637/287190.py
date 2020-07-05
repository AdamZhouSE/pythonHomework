n=(int)(input())
arr=list(map(int,input().split(' ')))
odd=0
even=0
for i in arr:
    if(i%2==0):
        even+=1
    else:
        odd+=1
turn=1 if odd>even else 0
while(len(arr)>0):
    record_i=-1
    record_num=-1
    for i in range(len(arr)):
        if((arr[i]-turn)%2==0 and arr[i]>record_num):
            record_i=i
            record_num=arr[i]
    if(record_i==-1):
        break
    else:
        del arr[record_i]
        turn=1-turn
print(sum(arr))