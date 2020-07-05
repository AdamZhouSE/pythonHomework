def getInvCount(arr, n):   
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count

t = int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    print(getInvCount(arr,n))