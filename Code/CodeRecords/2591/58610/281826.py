def is_prime(num):
    from math import sqrt
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0: return False
    return True

for _ in range(eval(input())):
    number = eval(input()) + 2
    print('Yes') if is_prime(number) else print('No')