inp_l = [i for i in input()]
inp_l.sort()
inp_str = ''
for i in inp_l:
    inp_str += i
is_ok = False
i = 0
while (2 ** i) < (10 ** 9):
    t = str(2 ** i)
    t_l = [i for i in t]
    t_l.sort()
    t_str = ''
    for j in t_l:
        t_str += j
    if t_str == inp_str:
        is_ok = True
        break
    i += 1
if is_ok:
    print('true')
else:
    print('false')
