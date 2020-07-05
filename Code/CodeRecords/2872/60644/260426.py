num=int(input())
arr=list(input())
start=arr[0]
i=1
res=0
while i<len(arr):
    try:
        if arr[i]==start:
            arr.remove(arr[i])
            i=i-1
            res=res+1
        else:
            start=arr[i]
    except:
        break
    i=i+1
print(res)
