t = int(input())
for index in range(t):
    length = int(input())
    arr1 = input().split(" ")
    arr2 = []
    for i in range(length-1):
        arr2.append(int(arr1[i]) ^ int(arr1[i+1]))
    arr2.append(int(arr1[length-1]))
    print(*arr2)