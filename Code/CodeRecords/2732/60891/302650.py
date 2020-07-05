t = int(input())
ans_l = []
for i in range(t):
    a_b_c = [int(i) for i in input().split()]
    a = a_b_c[0]
    b = a_b_c[1]
    c = a_b_c[2]
    res = (a ** b) % c
    ans_l.append(res)
for i in ans_l:
    print(i)