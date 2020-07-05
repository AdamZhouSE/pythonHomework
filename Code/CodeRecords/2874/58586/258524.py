n=int(input())
arr=list(map(int,input().split(" ")))
count=0
i=0
pre=""
while i<n:
    if arr[i]==0:
        count+=1
        i+=1
        pre=""
    else:
        if pre=="g":
            if arr[i]==2:
                pre=""
                count+=1
            else:
                pre="c"
            i+=1
        elif pre=="c":
            if arr[i]==1:
                pre=""
                count+=1
            else:
                pre="g"
            i+=1
        else:
            if arr[i]==1:
                pre="c"
            elif arr[i]==2:
                pre="g"
            i+=1
# if count==26:
#     print(n)
#     print(arr)
# else:
print(count)