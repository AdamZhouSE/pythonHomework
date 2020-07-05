carr=input().split(",")
arr=[]
for i in carr:
    i=int(i)
    arr.append(i)
dif=int(input())
count=1
res=1
for i in range(1, len(arr)):
    if arr[i]-arr[i-1]==dif:
        count=count+1
        res=max(res,count)
    else:
        count=1
print(res)   