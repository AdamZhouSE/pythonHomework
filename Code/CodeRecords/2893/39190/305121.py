def func9(arr):
    arr.sort()
    for i in range(0,len(arr),3):
        if i==len(arr)-1:
            return arr[i]
        elif arr[i]!=arr[i+1]:
            return arr[i]

arr=eval(input())
op=func9(arr)
print(op)
    