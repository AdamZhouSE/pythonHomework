def func31():
    in_str = input()[1:-1]
    rest = []
    while True:
        start = in_str.find("[")
        if start == -1:
            break
        end = in_str.find("]")
        rest.append(list(map(int, in_str[start+1:end].split(","))))
        in_str = in_str[end+1:]
    f = int(input())
    ans = []
    if f == 1:
        for i in rest:
            if i[2] == 1:
                ans.append(i)
    else:
        ans = rest.copy()
    max_p = int(input())
    i = 0
    while i < len(ans):
        if ans[i][3] <= max_p:
            i += 1
        else:
            ans.remove(ans[i])
    max_d = int(input())
    i = 0
    while i < len(ans):
        if ans[i][4] <= max_d:
            i += 1
        else:
            ans.remove(ans[i])
    ans.sort(key=lambda x:x[1])
    ans.reverse()
    res = []
    for i in ans:
        res.append(i[0])
    print(res)

    return
func31()