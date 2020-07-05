import re

def my_find(alpha_list):
    len_ = 0
    index = 0
    for i in range(len(alpha_list)):
        if len(alpha_list[i]) > len_:
            len_ = len(alpha_list[i])
            index = i
        elif len(alpha_list[i]) == len_:
            if alpha_list[i] < alpha_list[index]:
                index = i
    return alpha_list[index]


title = input()
pattern = re.compile('[a-z]+')
result = pattern.findall(input())
a = dict()
title = list(title)
for i in title:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

while len(result) >= 1:
    flag = True
    b = list(my_find(result))
    for i in b:
        if i not in a:
            flag = False
            break
    if flag:
        print(my_find(result))
        break
    else:
        result.remove(my_find(result))

