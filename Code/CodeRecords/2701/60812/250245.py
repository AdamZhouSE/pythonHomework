def win1(s):
    for i in range(3):
        if ((i, 0) in s and (i, 1) in s and (i, 2) in s) or ((0, i) in s and (1, i) in s and (2, i) in s):
            return True
    return False


def win2(s):
    if ((0, 0) in s and (1, 1) in s and (2, 2) in s) or ((0, 2) in s and (1, 1) in s and (2, 0) in s):
        return True
    return False


step = [(int(i[0]), int(i[2])) for i in input()[2:-2].split('],[')]
n = len(step)
A_step = step[::2]
B_step = step[1::2]
if win1(A_step) or win2(A_step):
    print('A')
elif win1(B_step) or win2(B_step):
    print('B')
elif n < 9:
    print('Pending')
else:
    print('Draw')
