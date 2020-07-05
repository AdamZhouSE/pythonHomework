n = int(input())
n_copy = n
part_num = n / 4
remain = n % 4
if remain == 3:
    remain = 6
if n < 4:
    print(remain)
else:
    result = -remain + int((n * (n - 1)) / (n - 2)) + (n - 3)
    n -= 4
    for i in range(int(part_num) - 1):
        result -= int((n * (n - 1)) / (n - 2)) - (n - 3)
        n -= 4
    print(result)