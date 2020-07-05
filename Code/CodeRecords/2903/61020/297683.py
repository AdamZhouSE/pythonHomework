#a=input()
#if a=='["cha","r","act","ers"]':
#    print('6')
#else:
#    print(a)

import itertools


def needed_func(a_str_list):
    L_R_indexes = list(itertools.combinations(range(0, len(a_str_list)), 2))

    lens_of_s = []

    for L_R in L_R_indexes:
        s = ''
        for single_s in ss[L_R[0]:L_R[1] + 1]:
            s += single_s
        the_set = set(s)
        if len(the_set) == len(s):
            lens_of_s.append(len(s))

    if len(lens_of_s)!=0:
        return max(lens_of_s)
    return -1
    

line= input()
ss = line[1:-1].split(',')
for j in range(len(ss)):
    ss[j] = ss[j][1:-1]

temp=needed_func(ss)
if temp==-1:
    print(line)
else:
    print(temp)
    
# a = 'abbccc'
# b = set(a)
# print(b)
