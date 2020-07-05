n = int(input())
for h in range(n):
    tem = input().split(' ')
    a = int(tem[0])
    b = int(tem[1])

    for x in range(a,b+1):
        judge = True
        for y in range(2,x):
            if x == 2:
                judge = True
                break
            elif x % y == 0:
                judge = False
        if judge:
            print(x,end = ' ')
    print()