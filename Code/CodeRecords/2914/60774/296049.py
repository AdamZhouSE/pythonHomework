t = int(input())
for i in range(0,t):
    n = int(input())
    arr1 = list(map(int,input().split(' ')))
    arr2 = list(map(int,input().split(' ')))
    flag1 = True
    flag2 = False
    k = 0
    for j in range(0,n):
        arr1[j] = arr1[j] - arr2[j]
        if(arr1[j] != 0 and flag1):
            flag1 = False
            flag2 = True
            k = arr1[j]
        elif(arr1[j] != k and flag2):
            flag2 = False
        elif(arr1[j] != 0 and not flag1 and not flag2):
            print('NO')
            break
    else:
        print('YES')