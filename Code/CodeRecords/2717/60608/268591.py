def func10():
    arr = eval(input())
    res = {'0': 0}
    ans = True
    for item in arr:
        if item[1] == '=':
            if item[0] in res.keys() and not item[3] in res.keys():
                res[item[3]] = res[item[0]]
            elif not item[0] in res.keys() and item[3] in res.keys():
                res[item[0]] = res[item[3]]
            elif item[0] in res.keys() and item[3] in res.keys() and res[item[0]] != res[item[3]]:
                val = res[item[0]]
                tem = res[item[3]]
                for key in res.keys():
                    if res[key] == tem:
                        res[key] = val
            else:
                val = max(res.values()) + 1
                res[item[0]] = val
                res[item[3]] = val
    for item in arr:
        if item[1] == '!':
            if item[0] in res.keys() and item[3] in res.keys() and res[item[0]] == res[item[3]]:
                ans = False
                break
    if ans:
        print('true')
    else:
        print('false')


func10()
