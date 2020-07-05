def func(arr: list):
    length=len(arr)
    for i in range(1,length-1):
        if arr[i]>arr[i+1] and arr[i]>arr[i]-1:
            return i
        elif arr[i]>arr[i+1]:
            i=i+1

a = input()
arr = list(map(int, a.split(',')))
arr=[-9999]+arr+[999999]
res=func(arr)
if res==None:
    res=len(arr)-1

print(res)