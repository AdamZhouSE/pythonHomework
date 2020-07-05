T = int(input())

for i in range(T):
    n = int(input())
    if n % 3 != 0:
        print(-1)

    else:
        mid_num = n // 3
        print(str(mid_num - 1) + ' ' + str(mid_num) + ' ' + str(mid_num + 1))
