t = int(input())
for i in range(t):
    a = input().split(" ")
    b = input().split(" ")
    a = list(map(int, a))
    b = list(map(int, b))
    result = a[0] < b[2] and b[0] < a[2] and a[1] > b[3] and b[1] > a[3]
    if result:
        print(1)
    else:
        print(0)