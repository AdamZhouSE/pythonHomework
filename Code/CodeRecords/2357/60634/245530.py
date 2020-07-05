problems = int(input())
for p in range(problems):
    temp = input().split(" ")
    N = int(temp[0])
    M = int(temp[1])
    X = int(temp[2])
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    
    ifExist = False
    i = 0
    while i < N:
        arr1[i] = int(arr1[i])
        j = 0
        while j < M:
            arr2[j] = int(arr2[j])
            if arr1[i]+arr2[j] == X:
                print(arr1[i],arr2[j])
                ifExist = True
            j += 1
        i += 1
    if not ifExist:
        print(-1)