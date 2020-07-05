times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    num_list = ["%0{}d".format(num_int) % int(bin(i).split("b")[1]) for i in range(2 ** num_int)]
    count = 0
    for i in num_list:
        if "11" in i:
            count += 1
    print(count)
    