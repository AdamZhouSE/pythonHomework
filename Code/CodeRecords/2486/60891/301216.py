def transform(inp_l):
    ans_l = []
    inp_l_len = len(inp_l)
    j = 0
    while j < inp_l_len:
        if str.isnumeric(inp_l[j]):
            times = int(inp_l[j])
            k = j + 1
            cnt = 0
            end_ = 0
            while k < inp_l_len:
                if inp_l[k] == '[':
                    cnt += 1
                elif inp_l[k] == ']':
                    cnt -= 1
                    if cnt == 0:
                        end_ = k
                        break
                k += 1
            for k in range(times):
                for m in range(j + 2, end_):
                    ans_l.append(inp_l[m])
            j = end_ + 1
        else:
            ans_l.append(inp_l[j])
            j += 1
    return ans_l


t = int(input())
res_li = []
for i in range(t):
    inp = input()
    j = 0
    inp_l = []
    ans = ''
    while j < len(inp):
        if str.isnumeric(inp[j]):
            be = j
            en = j + 1
            for k in range(j + 1, len(inp)):
                if not str.isnumeric(inp[k]):
                    en = k
                    break
            nu = int(inp[be:en])
            inp_l.append(str(nu))
            j = en

        else:
            inp_l.append(inp[j])
            j += 1
    while '[' in inp_l:
        inp_l = transform(inp_l)
    res_ = ''
    for j in inp_l:
        res_ += j
    res_li.append(res_)
for i in res_li:
    print(i)
