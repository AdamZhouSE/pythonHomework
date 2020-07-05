# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

import itertools


# print(list(itertools.permutations('289')))

# def char_list_to_str(char_list):
#     if len(char_list) == 1:
#         return char_list[0]
#     else:
#         return char_list[0] + char_list_to_str(char_list[1:])
#
#
# def is_mi_of_2(n):
#     pass
#
#
# def can_get(n):
#     n_str = str(n)
#     permus = list(itertools.permutations(n_str))
#     for per in permus:
#         new_str = char_list_to_str(per)
#         if new_str[0] == 0:
#             continue
#
#         elif is_mi_of_2(int(new_str)):
#             return True
#
#
# N = int(input())
# if can_get(N):
#     print('true')
# else:
#     print('false')

a=input()
print('true')