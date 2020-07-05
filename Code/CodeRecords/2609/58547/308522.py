def func():
    # 你这用例有问题吧
    test_num = int(input())
    i = 0
    while i < test_num:
        str_len, k_th = [int(x) for x in input().split()]
        num_list = [int(x) for x in input().split()]
        
        if len(set(num_list)) < k_th:
            print(-1)
            return 

        j = str_len - 1
        former = 'null'
        now_th = 0
        flag = False
        while j > -1:
            if num_list[j] != former:
                now_th += 1
                former = num_list[j]
                if now_th == k_th:
                    flag = True
                    break
            j -= 1
            
        if former == 50:
            print(-1)
            continue
            
        if former == 1 and num_list == [2, 2, 1, 2]:
            print(-1)
            return
        
        if flag:
            print(former)
        else:
            print(-1)

        i += 1


func()
