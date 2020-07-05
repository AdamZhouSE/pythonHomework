tests = input().split()
comd = int(tests[0])
D = int(tests[1])
t = 0
res = []
for i in range(0,comd):
    ls = input()
    com = ls[0]
    num = int(ls[1:])
    if com == 'A':
        res.append((num+t)%D)
    else:
        t = max(res[len(res)-num:])
        print(max(res[len(res)-num:]))