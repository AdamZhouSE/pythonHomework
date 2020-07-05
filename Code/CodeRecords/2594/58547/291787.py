def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        string = input()
        str_set = list(set(list(string)))
        
        if len(str_set) == len(string):
            print(-1)
            return 

        max_len = 0
        for target in str_set:
            j = 0
            L, R = -1, -1
            while j < len(string):
                if string[j] == target:
                    L = j
                    break
                j += 1
            j = len(string) - 1
            while j > -1:
                if string[j] == target:
                    R = j
                    break
                j -= 1
            max_len = max(max_len, R - L - 1)

        print(max_len)

        i += 1


func()
