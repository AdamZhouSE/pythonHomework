num = int(input())
for i in range(num):
    n = int(input())
    arr1 = sorted(list(map(int, input().split(" "))))
    a = 0
    b = 0
    temp = 0
    for item in arr1:
        if item - temp == 0:
            b = item
        elif item - temp != 1:
            a = item-1
        temp = item
    print(b,a)
