l = list((2 ** i) for i in range(0, 100))
times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    if num_int == 1:
        print(1)
    else:
        while(num_int not in l):
            num_int += 1
        print(num_int)