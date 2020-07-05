times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    p_int = 0
    sum_int = 0
    for i in range(1, num_int + 1):
        temp_int = 1
        for j in range(i):
            p_int += 1
            temp_int *= p_int
        sum_int += temp_int
    print(sum_int)