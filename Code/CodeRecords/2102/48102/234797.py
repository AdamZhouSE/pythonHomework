def prime_count2():
    num = int(input())

    if num < 2:
        print(0)
        return

    ls = [1] * num
    ls[0] = ls[1] = 0

    for i in range(2, int(num ** 0.5) + 1):
        if ls[i]:
            ls[i * i:num:i] = [0] * ((num - 1 - i * i) // i + 1)

    print(sum(ls))
    return


prime_count2()