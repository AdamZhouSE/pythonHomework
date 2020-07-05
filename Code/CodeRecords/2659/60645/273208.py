times_int = int(input())
for time in range(times_int):
    A_int, B_int = map(int, input().split(" "))
    print(B_int - A_int - 1)