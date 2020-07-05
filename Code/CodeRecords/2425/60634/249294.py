test = int(input())
for t in range(test):
    temp = input().split(" ")
    n = int(temp[0])
    k = int(temp[1])
    arr = input().split(" ")
    
    result = int(arr[0])
    c = abs(k - result)
    i = 1
    while i < n:
        if c >= abs(k - int(arr[i])):
            c = abs(k - int(arr[i]))
            result = int(arr[i])
        else:
            break
        i += 1
    print(result)
    