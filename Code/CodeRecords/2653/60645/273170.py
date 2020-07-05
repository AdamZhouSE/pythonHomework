times_int = int(input())
for time in range(times_int):
    A_int, B_int = map(int, input().split(" "))
    print((A_int - 1) * (10 - B_int))