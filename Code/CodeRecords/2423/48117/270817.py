questNum = int(input())

for quest in range(questNum):
    mn =input().split(' ')
    m = int(mn[0])
    n = int(mn[1])
    arr1 = input().split(' ')
    arr2 = input().split(' ')

    isSub = True
    for num in arr2:
        if not (num in arr1):
            isSub = False

    if isSub:
        print('Yes')
    else:
        print('No')