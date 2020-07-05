times_int = int(input())
for time in range(times_int):
    num = int(input())
    i = 0
    while(2 ** i <= num):
        i += 1
    print("{} {}".format(2 ** i - num - 1, 2 ** i - 1))