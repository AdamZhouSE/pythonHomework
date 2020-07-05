from math import sqrt

def is_prime_num(num):
    num_int = int(num)
    if num_int == 1:
        return False
    for i in range(2, int(sqrt(num_int)) + 1):
        if num_int % i == 0:
            return False
    return True

def find_prime_num(start, end):
    start_int = int(start)
    end_int = int(end)
    result_list = []
    for num in range(start_int, end_int + 1):
        if is_prime_num(num):
            result_list.append(str(num))
    return result_list

times_int = int(input())
for time in range(times_int):
    start, end = input().split(" ")
    start_int = int(start)
    end_int = int(end)
    print(" ".join(find_prime_num(start_int, end_int)))