n = int(input())
for h in range(n):
    num = int(input())
    x = num
    judge = True
    print(x,end = " ")
    while True:
        if x <= 0:
            judge = False
        if x > 0 and judge:
            x = x - 5
        else:
            x = x + 5
        print(x,end = " ")
        if x == num:
            break
    print()
            