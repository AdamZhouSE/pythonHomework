times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    sum_int = 1
    for verticle_num in range(1, num_int // 2 + 1):
        horizon_num = num_int - 2 * verticle_num
        temp = horizon_num + 1
        temp_sum = 1
        for i in range(verticle_num):
            temp_sum = temp * temp_sum
            temp += 1
        sum_int += (temp_sum // verticle_num)
    print(sum_int)