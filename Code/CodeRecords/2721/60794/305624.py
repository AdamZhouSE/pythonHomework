num = int(input())
for i in range(num):
    a = input().split(" ")
    b = int(a[0], 2)
    c = int(a[1], 2)
    print(b*c)