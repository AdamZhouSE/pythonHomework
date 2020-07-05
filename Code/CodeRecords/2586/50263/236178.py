a = eval(input())
b = eval(input())
c = eval(input())
s = []
d1 = abs(b-a)
d2 = abs(c-b)
min_move = 0
max_move = d1+d2-2
if max_move != 0:
    if min(d1,d2) < 3:
        min_move = 1
    else:
        min_move = 2
s.append(min_move)
s.append(max_move)
print(s)