def solve(string, all, res):
    for i in range(len(all)):
        s = string + all[i]
        temp = all.copy()
        temp.remove(all[i])
        solve(s, temp, res)
    if len(all) == 0:
        res.append(string)
    return res


s = input()[1:-1].split(",")
l = solve("", s, [])
for i in range(len(l)):
    l[i] = int(l[i])
print(max(l))