def func(arr: list):
    length=len(arr)
    for i in range(length-1):
        if i==0:
            if arr[i]>arr[i+1]:
                return i
        if arr[i]>arr[i+1] and arr[i]>arr[i]-1:
            return i
        elif arr[i]>arr[i+1]:
            i=i+1

a = input()
arr = list(map(int, a.split(',')))
res=func(arr)
if res==None:
    res=len(arr)-1

print(res)