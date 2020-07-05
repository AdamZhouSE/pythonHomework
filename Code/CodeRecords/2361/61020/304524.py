import math
import itertools


def is_square_num(n):
    r = int(math.floor(math.sqrt(n)))
    return r * r == n


def is_square_arr(arr):
    if len(arr) == 2:
        return is_square_num(sum(arr))

    if len(arr) > 2:
        return is_square_arr(arr[0:2]) and is_square_arr(arr[1:])


def num_of_permus(a_list):
    result = 0
    permus = list(itertools.permutations(a_list))

    prossed_permus = []
    for per in permus:
        if is_square_arr(per) and (per not in prossed_permus):
            result += 1
            prossed_permus.append(per)

    return result


A = input().split(',')
for i in range(len(A)):
    A[i] = int(A[i])

print(num_of_permus(A))
