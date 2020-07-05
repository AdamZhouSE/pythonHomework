def func12(arr,nums):
    if nums<3:
        return 0
    count=0
    for i in range(1,nums-1):
        if int(arr[i])<int(arr[i+1]) and int(arr[i])<int(arr[i-1]):
            count=count+1
        elif int(arr[i])>int(arr[i+1]) and int(arr[i])>int(arr[i-1]):
            count=count+1
    return count

nums=int(input())
arr=input().split(" ")
op=func12(arr,nums)
print(op)