def func(arr: list):
    length=len(arr)
    for i in range(1,length-1):
        if arr[i]>arr[i+1] and arr[i]>arr[i]-1:
            return i
        

a = input()
arr = list(map(int, a.split(',')))
print(func(arr))