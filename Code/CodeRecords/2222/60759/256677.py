import re


expre = input().replace('+', ' ').replace('-', ' -').split('=')
lst_x_l = re.findall('[+-]*\d*x', expre[0])
lst_x_r = re.findall('[+-]*\d*x', expre[1])
lst_d_l = list(map(int, re.findall('([+-]*\d)[^x]', expre[0] + ' ')))
lst_d_r = list(map(int, re.findall('([+-]*\d)[^x]', expre[1] + ' ')))
for i in lst_x_l:
    lst_x_l[lst_x_l.index(i)] = int(i.replace('x', '' if re.search('\d', i) else '1'))
for i in lst_x_r:
    lst_x_r[lst_x_r.index(i)] = int(i.replace('x', '' if re.search('\d', i) else '1'))
val_l = sum(lst_x_l) - sum(lst_x_r)
val_r = sum(lst_d_r) - sum(lst_d_l)
if val_l == 0:
    if val_r != 0:
        print('No solution')
    else:
        print('Infinite solutions')
else:
    print('x={}'.format(val_r/val_l))
