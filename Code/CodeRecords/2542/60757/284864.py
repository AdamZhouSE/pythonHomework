arr=sorted(eval(input()))
maxcount=1
count=1
for i in range(1,len(arr)):
    if arr[i]-arr[i-1]==1:
        count+=1
    else:
        if count>maxcount:
            maxcount=count
        count=1
print(maxcount)