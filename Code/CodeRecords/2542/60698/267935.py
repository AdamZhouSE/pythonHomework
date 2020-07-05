arr=list(eval(input()))
arr.sort()
if len(arr)<=1:
    print(len(arr))
else:
    length=1
    count=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            count=count+1
        else:
            if length<count:
                length=count
            count=1
    print(length)
