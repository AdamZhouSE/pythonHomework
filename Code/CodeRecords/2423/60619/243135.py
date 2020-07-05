t = int(input())
for index in range(t):
    li = input().split(" ")
    len1 = int(li[0])
    len2 = int(li[1])
    arr1 = input().split()
    arr2 = input().split()
    result = True
    for s in arr2:
        if s in arr1:
            index = arr1.index(s)
            del(arr1[index])
        else:
            result = False
            break
    if result:
        print("Yes")
    else:
        print("No")