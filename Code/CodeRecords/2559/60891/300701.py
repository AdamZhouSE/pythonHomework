n = int(input())
ans_l = []
for i in range(n):
    inp = input()
    len_inp = len(inp)
    inp_l = []
    for j in range(len_inp):
        inp_l.append(inp[j])
    inp_set = set(inp_l)
    len_set = len(inp_set)
    if len_inp == len_set:
        ans_l.append(1)
    else:
        ans_l.append(0)

for i in ans_l:
    print(i)