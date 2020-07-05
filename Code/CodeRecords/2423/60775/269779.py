result = 'Yes'

test = int(input())
for i in range(test):
    uselss = input()
    arr1 = [int(x) for x in input().split(' ')]
    arr2 = [int(x) for x in input().split(' ')]
    arr1.sort()
    arr2.sort()

    for x in arr2:
        if x not in arr1:
            result = 'False'
            break

    print(result)
