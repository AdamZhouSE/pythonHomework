n = int(input())
temp = [0, 1, 2, 6, 7]
if n <= 4:
    print(temp[n])
else:
    res = n + 1 + n - 3
    n -= 4
    four_times = n // 4
    remainder = n % 4

    if remainder:
        res = res + (-4) * four_times - temp[remainder]
    else:
        res = res + (-4) * (four_times - 1) - 5
    print(res)