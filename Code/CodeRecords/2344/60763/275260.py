T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, ('' + input()).split(' ')))
    d = int(input())
    for j in range(d):
        b = arr[0]
        arr.remove(b)
        arr.append(b)
    for j in arr:
        print(j,end=' ')
    print()