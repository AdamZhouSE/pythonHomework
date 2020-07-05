maxl=0
arr=eval(input())
if len(arr)>=2:
    arr=sorted(arr)
    for i in range(0,len(arr)-1):
        maxl=max(arr[i+1]-arr[i],maxl)
print(maxl)