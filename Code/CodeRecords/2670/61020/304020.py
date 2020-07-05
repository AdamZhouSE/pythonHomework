def pos_of_first_one(n):
    if n == 1:
        return 0
    return pos_of_first_one(n // 2) + 1


def needed_func(n):
    return ((2 ** (pos_of_first_one(n) + 1) - 1) | n) ^ n


T = int(input())
for i in range(T):
    print(needed_func(int(input())))
