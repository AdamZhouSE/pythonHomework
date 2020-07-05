arr=eval(input())
so=sorted(arr)
if arr==so:
    print(0)
else:
    start=0
    end=len(arr)
    for i in range(len(arr)):
        if arr[i]!=so[i]:
            start=i
            break
    for i in range(len(arr)-1,-1,-1):
        if arr[i]!=so[i]:
            end=i
            break
    print(end-start+1)