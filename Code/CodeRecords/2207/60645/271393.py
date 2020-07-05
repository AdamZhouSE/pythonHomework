# ?
times_int = int(input())
for time in range(times_int):
    A_int, B_int = map(int, input().split(" "))
    sum = 0
    for i in range(B_int):
        sum += i + 1
    if sum > A_int:
        print(0)
    else:
        print(1)