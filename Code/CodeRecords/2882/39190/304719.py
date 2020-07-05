def func3(arr):
    arr.reverse()
    rra=arr
    arr.reverse()
    peak=max(arr)
    if arr.index(peak)>0:
        for i in range(arr.index(peak)-1):
            if int(arr[i])>=int(arr[i+1]):
                return False
    if arr.index(peak)<len(arr)-rra.index(peak)-1:
        for i in range(arr.index(peak),len(arr)-rra.index(peak)-2):
            if int(arr[i])!=int(arr[i+1]):
                return False
    if rra.index(peak)>0:
        for i in range(len(arr)-rra.index(peak)-1,len(arr)-1):
            if int(arr[i])<=int(arr[i+1]):
                return False
    return True
ip=input()
arr=input().split(" ")
op=func3(arr)
if op==True:
    print("YES")
else:
    print("NO")