All = int(input())

for q in range(0, All):
    temp = input().split()
    N = int(temp[0])
    x = int(temp[1])

    a = []
    for i in range(0, N):
        a = a + input().split()
    b = []
    for i in range(0, N):
        b = b + input().split()

    num = 0
    for i in range(0, N * N):
        t = x- int(a[i]) 
        t=str(t)
        if t in b:
            num += 1
    print(num)
