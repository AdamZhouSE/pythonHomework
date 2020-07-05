for h in range(int(input())):
    tem = input().split(' ')
    a = int(tem[0])
    b = int(tem[1])
    x = a + b
    while True:
        x = x + 1
        judge = True
        for y in range(2,x):
            if x == 2:
                judge = True
                break
            elif x % y == 0:
                judge = False
        if judge and x != 1:
            print(x-a-b)
            break