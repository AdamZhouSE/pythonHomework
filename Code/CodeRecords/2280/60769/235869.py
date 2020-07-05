num = int(input())
for i in range(num):
    n = int(input())
    arr1 = list(map(int, input().split(" ")))
    for j in range(1,n+1):
        if not j in arr1:
            print(j)
            break