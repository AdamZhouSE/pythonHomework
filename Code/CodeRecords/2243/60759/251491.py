def get_point():
    p = eval(input())
    q = eval(input())
    if q == 0:
        return 0
    x = p * p / q
    is_up = True
    while x % p != 0:
        x *= 2
        is_up = False if is_up else True
    if is_up:
        return 1 if (x / p) % 2 else 2
    return 0


print(get_point())
