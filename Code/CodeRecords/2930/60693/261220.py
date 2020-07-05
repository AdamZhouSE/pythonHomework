def find_extre(arr,n):
    if n<3:return 0
    res=0
    for i in range(1,n-1):
        if (arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i-1] and arr[i]<arr[i+1]):
            res+=1
    return res

n=int(input())
arr=list(map(int,input().split()))
print(find_extre(arr,n))