n = int(input())
if n < 1:
    print(str(1))
else:
    count = 0
    base = 1
    round = n
    while round > 0:
        weight = round % 10
        round = int(round / 10)
        count += round * base
        if weight == 1:
            count += (n % base) + 1
        elif weight > 1:
            count += base
        base *= 10
    print(str(count))