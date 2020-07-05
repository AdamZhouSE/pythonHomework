
def func14():
    n, ops, res = eval(input()), [], []
    for i in range(0, n):
        ops.append(input().split())
    for i in range(0, n):
        t = ops[i]
        if t[0] == 'A':
            ans = []
            for j in range(0, len(res)):
                if (res[j][0] <= int(t[2]) and res[j][1] >= int(t[1])) or (
                        res[j][1] >= int(t[1]) and res[j][0] <= int(t[2])):
                    ans.append(res[j])
            for k in range(0, len(ans)):
                res.remove(ans[k])
            res.append((int(t[1]), int(t[2])))
            print(len(ans))
        elif t[0] == 'B':
            print(len(res))


func14()
