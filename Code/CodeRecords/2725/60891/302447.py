t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    if n == 2:
        ans_l.append(1)
    elif n == 3:
        ans_l.append(0)
    elif n == 4:
        ans_l.append(1)
    elif n%2==0:
        ans_l.append(1)
    else:
        ans_l.append(0)
for i in ans_l:
    print(i)