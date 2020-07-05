test_num = int(input())
for i in range(test_num):
    n = int(input())
    array1 = input().split(" ")
    array2 = input().split(" ")
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    array1.sort()
    array2.sort()
    sentinel = 0
    for j in range(len(array1)):
        if array1[j] != array2[j]:
            sentinel = 1
    if sentinel == 0:
        print(1)
    else:
        print(0)