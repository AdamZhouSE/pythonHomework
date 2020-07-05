times_int = int(input())
for time in range(times_int):
    A_int = list(bin(int(input())).split("b")[1])
    zero_count = 0
    one_count = 0
    for i in A_int:
        if i == "0":
            zero_count += 1
        else:
            one_count += 1
    print(zero_count ^ one_count)