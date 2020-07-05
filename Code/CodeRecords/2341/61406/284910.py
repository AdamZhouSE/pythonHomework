T = int(input())
for a in range(0,T):
    XY = input().split(' ')
    x = int(XY[0])
    y = int(XY[1])
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    ptr1 = 0
    ptr2 = 0
    result = ""
    for i in range(0,x):
        arr1[i]=int(arr1[i])
    for i in range(0,y):
        arr2[i]=int(arr2[i])
    arr1.sort()
    arr2.sort()
    while ptr1<x or ptr2<y:
        if ptr2==y:
            result = result + str(arr1[ptr1]) + " "
            ptr1 += 1
        elif ptr1==x:
            result = result + str(arr2[ptr2]) + " "
            ptr2 += 1
        elif arr1[ptr1]<arr2[ptr2]:
            result = result + str(arr1[ptr1])+" "
            ptr1+=1
        elif arr2[ptr2]<arr1[ptr1]:
            result = result + str(arr2[ptr2])+" "
            ptr2+=1
    print(result)
