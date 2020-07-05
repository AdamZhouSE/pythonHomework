times_int = int(input())
for time in range(times_int):
    num_list = list("0" + (bin(int(input())).split("b")[1]))
    for i in range(len(num_list)-1, 0, -2):
        temp_int = num_list[i]
        num_list[i] = num_list[i-1]
        num_list[i-1] = temp_int
    print(int("".join(num_list), 2))