arr=eval(input())
record=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        judge=True
        for k in arr[j]:
            if k in arr[i]:
                judge=False
                break
        if(judge and len(arr[i])*len(arr[j])>record):
            record=len(arr[i])*len(arr[j])
print(record)
