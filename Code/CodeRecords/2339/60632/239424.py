t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    count = 0
    for j in range(n):
        for k in range(j+1, n):
            if arr[j] > arr[k]:
                count += 1
    print(count)
