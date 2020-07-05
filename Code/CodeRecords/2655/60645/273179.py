times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    if num_int == 1:
        print(1)
    else:
        while(num_int % 2 != 0):
            num_int += 1
    print(num_int)