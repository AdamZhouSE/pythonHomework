test = int(input())
for i in range(0, test):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    a = arr[0]
    b = arr[-1]
    for j in range(1, a*b+1):
        if j % a == 0 and j % b == 0:
            print(j)
            break