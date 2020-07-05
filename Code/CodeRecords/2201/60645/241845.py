from math import sqrt

def is_prime_num(num):
    num_int = int(num)
    if num_int == 1:
        return False
    for i in range(2, int(sqrt(num_int)) + 1):
        if num_int % i == 0:
            return False
    return True

def find_prime_num(start):
    start_int = int(start)
    ptr_int = 1
    while True:
        if not is_prime_num(start_int + ptr_int):
            ptr_int += 1
            continue
        return ptr_int

times_int = int(input())
for time in range(times_int):
    temp_list = input().split(" ")
    start_int = int(temp_list[0]) + int(temp_list[1])
    print(find_prime_num(start_int))