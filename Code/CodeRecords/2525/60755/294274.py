def solve(s, start, end, pay):
    all = []
    st = start.copy()
    e = end.copy()
    p = pay.copy()
    for i in range(len(s)):
        if s[i] != "1":
            st.remove(start[i])
            e.remove(end[i])
            p.remove(pay[i])
    res = sum(p)
    flag = False
    for i in range(len(st)):
        for k in range(1, len(st)):
            if e[k] > e[i] > st[k] or e[i]>st[k]>st[i]:
                res = 0
                flag = True
                break
        if flag:
            break
    return res


start = input()[1:-1].split(",")
end = input()[1:-1].split(",")
pay = input()[1:-1].split(",")
for i in range(len(start)):
    start[i] = int(start[i])
    end[i] = int(end[i])
    pay[i] = int(pay[i])
all = []
for i in range(pow(2, len(start))):
    temp = bin(i)[2:]
    while len(temp) != len(start):
        temp = "0" + temp
    all.append(solve(temp, start, end, pay))
print(max(all))