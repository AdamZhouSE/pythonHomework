def findSub(S, size, arr):
    i = 0
    while i < size:
        count = S - int(arr[i])
        j = i + 1
        while j <= size:
            if j == size:
                if count == 0:
                    return [i + 1, i + 1]
                else:
                    break
            count -= int(arr[j])
            if count == 0:
                return [i + 1, j + 1]
            j += 1
        i += 1
    return -1


test = int(input())
for t in range(test):
    temp = input().split(" ")
    size = int(temp[0])
    S = int(temp[1])
    arr = input().split(" ")
    
    result = findSub(S,size,arr)
    if result == -1:
        print(-1)
    else:
        print(result[0],result[1])
    
    