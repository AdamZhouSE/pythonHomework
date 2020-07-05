arr=eval(input())
count = 1;
maxcount=1
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        count=count+1
    else:
        if count>maxcount:
            maxcount=count
        count=1
print(maxcount)