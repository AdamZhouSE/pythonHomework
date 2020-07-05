g=int(input())
for i in range(0,g):
    n=int(input())
    arr=input().split()
    for i in range(0,n):
        arr[i]=int(arr[i])
    for i in range(0,n):
        for j in range(0,n-1):
            if arr.count(arr[j])<arr.count(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            if arr.count(arr[j])==arr.count(arr[j+1]):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    s=''
    for i in range(0,n):
        s=s+' '+str(arr[i])
    print(s[1:]+' ')
