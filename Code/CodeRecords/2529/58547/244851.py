def func():
    number = int(input())
    number_str_sorted = sorted(str(number))
    i = 0
    while True:
        now_num = 2 ** i
        now_str_sorted = sorted(str(now_num))
        if len(number_str_sorted) > len(number_str_sorted):
            print("false")
            return
        if number_str_sorted == now_str_sorted:
            print("true")
            return
        i += 1


func()
