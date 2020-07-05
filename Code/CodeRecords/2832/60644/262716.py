num=int(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])-1
res=0
end=0
for i in range(0,len(arr)):
    try:
        if arr[i] == end:
            res = res + 1
            end = i + 1
    except:
        continue



    if arr[i]>end:
        end=arr[i]
print(res)