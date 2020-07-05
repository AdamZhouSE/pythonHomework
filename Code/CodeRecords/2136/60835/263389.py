n = int(input())
for x in range(2,n):
    tem = n
    judge = True
    while tem > 0:
        if tem % x != 1:
            judge = False
            break
        else:
            tem = tem // x
    if judge:
        print(x)
        break
    