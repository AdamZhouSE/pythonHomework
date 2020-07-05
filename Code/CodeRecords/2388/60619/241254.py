t = int(input())
for index in range(t):
    length = int(input())
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    isSame = True
    for i in arr1:
        if i not in arr2:
            isSame = False
            break
        else:
            index = arr2.index(i)
            del(arr2[index])
    if isSame:
        print(1)
    else:
        print(0)
