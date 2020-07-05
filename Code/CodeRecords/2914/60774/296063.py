t = int(input())
for i in range(0,t):
    n = int(input())
    arr1 = list(map(int,input().split(' ')))
    arr2 = list(map(int,input().split(' ')))
    if(arr1 == arr2):
        print('YES')
        continue
    flag1 = True
    flag2 = False
    count = 0
    k = 0
    for j in range(0,n):
        arr1[j] = arr1[j] - arr2[j]
        if(arr1[j] != 0 and flag1):
            flag1 = False
            flag2 = True
            k = arr1[j]
            count = 1
        elif(arr1[j] != k and flag2):
            flag2 = False
        elif(arr1[j] == k and flag2):
            count = count + 1
        elif(arr1[j] != 0 and not flag1 and not flag2):
            print('NO')
            break
    else:
        if(count > 1):
            print('YES')
        else:
            print('NO')