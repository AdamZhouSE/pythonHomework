def func():
    str_arr = ["" for x in  range(0, 3)]
    for i in range(0, 3):
        str_arr[i] = input()

    str_arr.sort()
    for ele in str_arr:
        print(ele)


func()
