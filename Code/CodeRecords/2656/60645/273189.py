times_int = int(input())
for time in range(times_int):
    A_int, B_int = map(bin, map(int, input().split(" ")))
    A_list = list(A_int.split('b')[1])
    B_list = list(B_int.split('b')[1])
    p_int = 1
    if A_int == B_int:
        print(-1)
    else:
        try:
            while True:
                if A_list[-p_int] != B_list[-p_int]:
                    print(p_int)
                    break
                p_int += 1
        except:
            print(p_int + 1)