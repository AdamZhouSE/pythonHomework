test = int(input())
for t in range(test):
    size = int(input())
    arr = input().split(" ")
    
    count = 1
    i = 0
    while i < size:
        if i == size-1:
            count = size
            break
        if int(arr[i]) != count:
            break
        i += 1
        count += 1
    print(count)