times_int = int(input())
for time in range(times_int):
    A_int, B_int = map(int, input().split(" "))
    num_list = [int(i) for i in input().split(" ") if (int(i) % B_int == 0)]
    result = 0
    for num in num_list:
        result = result | num
    print(result)