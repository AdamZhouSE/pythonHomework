
def func3():
    n, arr = eval(input()), eval(input())
    ans, need, tem = [], {i: [] for i in range(0, n)}, []

    for item in arr:
        need[item[0]].append(item[1])
    for key in need.keys():
        if not need[key]:
            ans.append(key)

    while len(ans) < n:
        flag = 1
        for key in need.keys():
            if key not in ans and need[key]:
                k = 1
                for val in need[key]:
                    if val not in ans:
                        k = 0
                        break
                if k:
                    flag = 0
                    ans.append(key)

        if flag and len(ans) != n:
            print([])
            return
    print(ans)


func3()
