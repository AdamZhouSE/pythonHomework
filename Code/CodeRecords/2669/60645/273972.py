times_int = int(input())
for time in range(times_int):
    num_int = int(input())
    print(" ".join([str(i) for i in range(num_int, -1, -1) if num_int & i == i]))