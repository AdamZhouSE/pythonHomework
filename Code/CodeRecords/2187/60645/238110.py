times_int = int(input())
for time_int in range(times_int):
    n, k = input().split(" ")
    n_int = int(n)
    k_int = int(k)
    nums_list = list(map(int, input().split(" ")))
    max_whole_int = 0
    temp_whole = 0
    for i in range(0, n_int - k_int + 1):
        if i!=0 and nums_list[i - 1] > nums_list[i + k_int - 1]:
            continue
        temp_whole_int = 0
        for l in range(k_int):
            temp_whole_int += nums_list[i + l]
            if temp_whole_int > max_whole_int:
                max_whole_int = temp_whole_int
    print(max_whole_int)