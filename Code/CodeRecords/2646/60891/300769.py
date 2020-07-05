t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        ans_l.append('PlayerA')
    else:
        ans_l.append('PlayerB')
for i in ans_l:
    print(i)
