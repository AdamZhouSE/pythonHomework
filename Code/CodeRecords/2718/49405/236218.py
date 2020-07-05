s = list(input())
moves = eval(input())
while True:
    f = True
    for move in moves:
        t = s
        t[move[0]], t[move[1]] = t[move[1]], t[move[0]]
        if ''.join(t) < ''.join(s):
            s = t
            f = False
    if f: break
print(''.join(s))