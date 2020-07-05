
test = int(input())
for i in range(test):
    result = 'Yes'

    inpu1 = input().split(' ')
    l1 = int(inpu1[0])
    l2 = int(inpu1[1])
    if l2 == 0:
        result = 'Yes'
    elif l2 > 1:
        arr1 = [int(x) for x in (input()).split(' ')]
        arr2 = [int(x) for x in (input()).split(' ')]
        for x in arr2:
            if x not in arr1:
                result = 'No'
                break
    elif l2 == 1:
        arr1 = [int(x) for x in (input()).split(' ')]
        arr2 = int(input())
        if arr2 not in arr1:
            result = 'No'

    print(result)
