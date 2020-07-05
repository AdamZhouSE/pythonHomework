n = int(input())
ans_l = []
for i in range(n):
    inp = input()
    inp_len = len(inp)
    tmp = inp[0]
    form = inp[0]
    for j in range(1, inp_len):
        if inp[j] != form:
            tmp += inp[j]
            form = inp[j]
    ans_l.append(tmp)
for i in range(len(ans_l)):
    print(ans_l[i])
