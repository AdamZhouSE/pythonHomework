def short(ls: list) -> int:
    len_ls = len(ls)
    if len_ls == 2 and ls[0] > ls[1]:
        return 2
    left1 = 0
    right1 = len_ls - 1
    for i in range(1, len_ls):
        if ls[i] < ls[i-1]:
            left1 = i - 1
            break
    for i in range(len_ls - 1, -1, -1):
        if ls[i] < ls[i-1]:
            right1 = i - 1
            break
    min_num = min(ls[left1:right1+1])
    max_num = max(ls[left1:right1+1])
    ls = ls[:left1] + sorted(ls[left1:right1+1]) + ls[right1+1:]
    ls.remove(min_num)
    ls.remove(max_num)
    left2 = 0
    right2 = len_ls - 2
    for i in range(len_ls - 2):
        if min_num >= ls[i]:
            left2 += 1
    for i in range(len_ls - 3, -1, -1):
        if max_num <= ls[i]:
            right2 -= 1
    return right2 - left2 + 2


lst = eval(input())
print(short(lst))