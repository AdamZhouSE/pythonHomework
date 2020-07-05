import itertools


def needed_func(a_str_list):
    if len(a_str_list) == 1:
        return len(a_str_list[0])

    L_R_indexes = list(itertools.combinations(range(0, len(a_str_list)), 2))

    lens_of_s = []

    for L_R in L_R_indexes:
        s = ''
        for single_s in ss[L_R[0]:L_R[1] + 1]:
            s += single_s
        the_set = set(s)
        if len(the_set) == len(s):
            lens_of_s.append(len(s))

    return max(lens_of_s)


ss = input()[1:-1].split(',')
for j in range(len(ss)):
    ss[j] = ss[j][1:-1]

print(needed_func(ss))

# a = 'abbccc'
# b = set(a)
# print(b)
