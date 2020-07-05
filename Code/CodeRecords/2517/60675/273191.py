def func(l : list) -> int:
    cnt = 0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    if l[0][a] + l[1][b] + l[2][c] + l[3][d] == 0:
                        cnt += 1
    return cnt


l, tmp = [], []
for i in range(4):
    string = "tmp = [" + input() + "]"
    exec(string)
    l.append(tmp)
print(func(l))