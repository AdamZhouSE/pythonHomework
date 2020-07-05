count = int(input())
for n in range(count):
    info = input().split()
    m = int(info[0])
    n = int(info[1])
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    flag = True
    for a in arr2:
        if a not in arr1:
            flag=False
            break
    if flag:
        print('Yes')
    else:
        print('No')