def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        P = int(input())
        P_cp = P
        T = int(input())
        R = int(input())
        j = 1
        while j <= T:
            P += P_cp * (R / 100)
            j += 1
        print(int(P - P_cp))
        i += 1


func()
