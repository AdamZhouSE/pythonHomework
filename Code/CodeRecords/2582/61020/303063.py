import math
import itertools


def my_abs(n):
    return int(math.fabs(n))


def target_func(arr1, arr2, i, j):
    # |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

    return my_abs(arr1[i] - arr1[j]) + my_abs(arr2[i] - arr2[j]) + my_abs(i - j)


arr1 = input().split(',')
arr2 = input().split(',')

for i in range(len(arr1)):
    arr1[i] = int(arr1[i])
    arr2[i] = int(arr2[i])

combs_of_indexes = list(itertools.combinations(range(len(arr1)), 2))

values = []
for comb in combs_of_indexes:
    values.append(target_func(arr1, arr2, comb[0], comb[1]))

print(max(values))
