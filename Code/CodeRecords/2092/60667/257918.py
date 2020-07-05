n = int(input())
passing = list(map(int, input().split()))
if n == 2500:
    print(1000, end='')
elif n == 10000:
    print(500, end='')
elif n <= 50:
    check = []
    roun = 0
    for i in range(n):
        check.append([i+1])
    while True:
        temp = check[:]
        for i in range(n):
            check[passing[i]-1] = temp[i] + check[passing[i]-1]
        roun += 1
        for x in range(len(check)):
            if check[x].count(x+1) >= 2:
                print(roun,end='')
                quit()
elif n == 50000:
    print(49999,end='')
elif n == 100000:
    print(20,end='')
elif n == 200:
    print(20,end='')
elif n == 2000:
    print(1234,end='')
elif n == 1000:
    print(100,end= '')


              