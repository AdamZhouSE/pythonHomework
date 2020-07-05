def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        bin_num_list = list(bin(int(input())))
        j = 2
        while j < len(bin_num_list):
            bin_num_list[j] = str(abs(int(bin_num_list[j]) - 1))
            j += 1
        print(eval("".join(bin_num_list)))
        i += 1


func()
