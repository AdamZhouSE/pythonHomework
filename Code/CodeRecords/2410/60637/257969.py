arr=eval(input())
difference=(int)(input())
result=1
for i in range(0,len(arr)):
    record=1
    num=(int)(arr[i])
    for j in range(i,len(arr)):
        if((int)(arr[j])-num==difference):
            num=(int)(arr[j])
            record+=1
    if(record>result):
        result=record
print(result)