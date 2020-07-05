T = int(input())
for i in range(T):
    m, n = [int(j) for j in input().split(' ')]
    arr1 = {int(j) for j in input().split(' ')}
    arr2 = {int(j) for j in input().split(' ')}
    s = 'Yes'
    for j in arr2:
        if j not in arr1:
            s = 'No'
            break
    print(s)