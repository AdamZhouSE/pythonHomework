def func(arr: list):
    length=len(arr)
    h=0
    maxi=arr[-1]
    for i in range(maxi+1):
        j=0
        while arr[j]<i:
            j+=1
        temp=length-j
        if i<=temp:
            h=i
    return h
b = input()
arr = list(map(int, b.split(',')))
print(func(arr))