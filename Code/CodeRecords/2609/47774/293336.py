num=int(input())
for nn in range(num):
    n,k=input().split(' ')
    k=int(k)
    arr=input().split(' ')
    res=-1
    count=0
    for i in range(len(arr)):
        j=0
        while j<len(arr):
            if (i != j and int(arr[j]) == int(arr[i])): 
                break
            j += 1
        if (j == len(arr)): 
            count += 1
        if (count == k): 
            res = int(arr[i])
            break
    print(res)