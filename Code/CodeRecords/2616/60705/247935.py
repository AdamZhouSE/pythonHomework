n = int(input())
for i in range(0, n):
    a = list(map(int, input().split(" ")))
    b = a[0]
    c = a[1]
    sum = 0
    for j in range(1, c+1):
        sum += j
    if sum <= b:
        print("1")
    else:
        print("0")
