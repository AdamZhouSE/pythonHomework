n = int(input())
ans_l = []
for i in range(n):
    inp = input()
    inp_l = []
    for j in range(len(inp)):
        inp_l.append(inp[j])
    inp_set = set()
    for j in inp_l:
        inp_set.add(j)
    len_set = len(inp_set)
    if len_set % 2 == 1:
        ans_l.append('HE!')
    else:
        ans_l.append('SHE!')
for i in ans_l:
    print(i)