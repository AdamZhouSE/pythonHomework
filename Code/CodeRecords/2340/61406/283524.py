T = int(input())
for a in range(0,T):
    n = int(input())
    arr = input().split(' ')
    for i in range(0,n):
        arr[i] = int(arr[i])
    sum = 0
    highest = max(arr)
    start = 0
    for ptr in range(0,arr.index(highest)):
        if arr[ptr]>=arr[start]:
            start = ptr
        elif arr[ptr]<arr[start]:
            sum = sum+arr[start]-arr[ptr]
    ptr = n-1
    start = ptr
    while ptr>arr.index(highest):
        if arr[ptr]>=arr[start]:
            start = ptr
        elif arr[ptr]<arr[start]:
            sum = sum+arr[start]-arr[ptr]
        ptr = ptr-1
    print(sum)



