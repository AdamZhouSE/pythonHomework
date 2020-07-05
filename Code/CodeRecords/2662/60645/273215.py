times_int = int(input())
for time in range(times_int):
    A_int = list(bin(int(input())).split("b")[1])
    one_count = 0
    for i in A_int:
        if i == "1":
            one_count += 1
    if one_count % 2 == 0:
        print("even")
    else:
        print("odd")