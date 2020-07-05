t = int(input())
for i in range(t):
    n = int(input())
    tmp = 1
    for i in range(31):
        tmp = tmp << 1 | 1
    print(tmp ^ n)
