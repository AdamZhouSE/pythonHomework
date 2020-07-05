t = int(input())
ans_l = []
for i in range(t):
    a_b = [i for i in input().split()]
    a = a_b[0]
    b = a_b[1]
    a_v = 0
    b_v = 0
    for j in range(len(a)):
        a_v += 2 ** j * int(a[len(a) - j - 1])
    for j in range(len(b)):
        b_v += 2 ** j * int(b[len(b) - j - 1])
    ans_l.append(a_v * b_v)
for i in ans_l:
    print(i)