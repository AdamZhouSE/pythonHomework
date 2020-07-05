import collections


def long_arr2():
    ls1 = list(eval(input()))
    ls2 = list(eval(input()))
    max_len = 0
    ls2_starts = collections.defaultdict(list)
    for index, item in enumerate(ls2):
        ls2_starts[item].append(index)
    for index, item in enumerate(ls1):
        for j in ls2_starts[item]:
            k = 0
            while index + k < len(ls1) and j + k < len(ls2) and ls1[index + k] == ls2[j + k]:
                k += 1
                max_len = max(max_len, k)
    return max_len


print(long_arr2())