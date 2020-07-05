test = int(input())
for t in range(test):
    temp = input().split(" ")
    m = int(temp[0])
    n = int(temp[1])
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    
    count = 0
    for x in arr2:
        i = 0
        while i < len(arr1):
            if int(x) == int(arr1[i]):
                count += 1
                arr1.remove(arr1[i])
                break
            i += 1
    
    if count == n:
        print("Yes")
    else:
        print("No")