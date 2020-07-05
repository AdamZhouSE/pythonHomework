t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    if n % 2 == 1:
        ans_l.append('Player A')
    else:
        ans_l.append('Player B')
for i in ans_l:
    print(i)
