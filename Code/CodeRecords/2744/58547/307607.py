def is_hw(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def func():
    s_num = int(input())
    arr = []
    for i in range(s_num):
        eat, temp = input().split()
        arr.append(temp)

    res_num = 0  # res_num != len(res)
    for i in range(s_num):
        for j in range(i, s_num):
            if is_hw(arr[i] + arr[j]):
                if i == j:
                    res_num += 1
                elif is_hw(arr[j] + arr[i]):
                    res_num += 2
                else:
                    res_num += 1

    print(res_num)


func()
