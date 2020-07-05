t = sorted([eval(input()), eval(input()), eval(input())])
max_move = t[2] - t[0] - 2
if t[2] - t[0] == 2:
    min_move = 0
elif t[2] - t[1] == 1 or t[1] - t[0] == 1:
    min_move = 1
elif t[2] - t[1] == 2 or t[1] - t[0] == 2:
    min_move = 1
else:
    min_move = 0
print([min_move, max_move])