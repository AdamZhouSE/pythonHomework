s = input()
s_len = len(s)
w_st = []
for bi in range(s_len):
    for ei in range(bi, s_len):
        w_st.append(s[bi:ei + 1])
w_s = set(w_st)
count = 0
while len(w_s) > 0:
    s = w_s.pop()
    is_odd = True
    s_len = len(s)
    s_b = s[0]
    ch_i = -1
    for i in range(s_len):
        if s[i] != s_b:
            ch_i = i
            break
    if ch_i != -1:
        for i in range(ch_i, s_len):
            if s[i] == s_b:
                is_odd = False
                break
    if is_odd:
        count += 1
print(count)
