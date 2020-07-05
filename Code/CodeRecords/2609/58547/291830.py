def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        str_len, k_th = [int(x) for x in input().split()]
        num_list = [int(x) for x in input().split()]

        j = str_len - 1
        former = 'null'
        now_th = 0
        while j > -1:
            if num_list[j] != former:
                now_th += 1
                former = num_list[j]
                if now_th == k_th:
                    break
            j -= 1

        if now_th == k_th:
            print(former)
        else:
            print(-1)

        i += 1


func()
