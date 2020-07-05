def swap(x1, x2, arr1,arr2):
    temp = arr1[x1]
    arr1[x1] = arr2[x2]
    arr2[x2] = temp


def filter(arr):
    i = len(arr) - 1
    while i > 0:
        if int(arr[i]) < int(arr[i-1]):
            swap(i,i-1,arr,arr)
        else:
            break
        i -= 1


def printArray(arr1,arr2):
    for x in arr1:
        print(x,end = " ")
    for x in arr2:
        print(x,end = " ")
    print()

problems = int(input())
for x in range(problems):
    temp = input().split(" ")
    n = int(temp[0])
    m = int(temp[1])
    arr1 = input().split(" ")
    arr2 = input().split(" ")

    point = len(arr2)-1
    top = len(arr1)-1
    while point >= 0:
        if int(arr1[top]) > int(arr2[point]):
            swap(top,point,arr1,arr2)
            filter(arr1)
        point -= 1

    printArray(arr1,arr2)
    
    