def get_count(formula):
    num_lst = []
    d_count = 0
    pre_o = '+'
    x_count = 0
    for ch in formula:
        if ch == '+' or ch == '-':
            if len(num_lst) != 0:
                d_count = eval(str(d_count) + pre_o + ''.join(num_lst))
                num_lst = []
            pre_o = ch
        elif ch == 'x':
            add_x = 1 if len(num_lst) == 0 else int(''.join(num_lst))
            x_count += add_x if pre_o == '+' else -add_x
            num_lst = []
        else:
            num_lst.append(ch)
    if len(num_lst) != 0:
        d_count = eval(str(d_count) + pre_o + ''.join(num_lst))
    return x_count, d_count


expre = input().split('=')
x1, d1 = get_count(expre[0])
x2, d2 = get_count(expre[1])
l = x1 - x2
r = d2 - d1
if l == 0:
    if r == 0:
        print('Infinite solutions')
    else:
        print('No solution')
else:
    print('x={}'.format(r/l))
