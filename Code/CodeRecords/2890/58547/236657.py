def func():
    temp_arr = [int(x) for x in input().split()]
    n = temp_arr[0]
    bias = [temp_arr[1], temp_arr[2]]
    all_pos = []

    i = 0
    while i < n:
        x, y = input().split(" ")
        x = int(x) - bias[0]
        y = int(y) - bias[1]
        if x == 0:
            all_pos.append("Inf")
        else:
            all_pos.append(y/x)
        i += 1

    print(len(set(all_pos)))


func()
