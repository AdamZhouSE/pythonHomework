def addarr(arr):
    n=arr.index(max(arr))
    for i in range(len(arr)):
        arr[i]=arr[i]+1
    arr[n]=arr[n]-1
    return arr
arr=list(eval(input()))
count=0
while(True):
    if arr.count(max(arr))==len(arr):
        print(count)
        break
    else:
        addarr(arr)
        count=count+1