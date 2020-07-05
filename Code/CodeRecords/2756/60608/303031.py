
def road(ans: list, des: int, red: dict, blue: dict, path: list, level: int, isred: bool):
    if path[-1] == des:
        if ans[des] == -1:
            ans[des] = level
        else:
            ans[des] = min(ans[des], level)
    else:
        if isred:
            for dot in red[path[-1]]:
                if dot not in path:
                    path.append(dot)
                    road(ans, des, red, blue, path, level + 1, not isred)
                    del path[-1]
        else:
            for dot in blue[path[-1]]:
                if dot not in path:
                    path.append(dot)
                    road(ans, des, red, blue, path, level + 1, not isred)
                    del path[-1]


def func9():
    n, arr1, arr2 = eval(input()), eval(input()), eval(input())
    ans = [-1 if i > 0 else 0 for i in range(0, n)]
    red, blue = {i: [] for i in range(0, n)}, {i: [] for i in range(0, n)}
    for i in range(0, len(arr1)):
        node = arr1[i]
        red[node[0]].append(node[1])
    for i in range(0, len(arr2)):
        node = arr2[i]
        blue[node[0]].append(node[1])

    for i in range(1, n):
        road(ans, i, red, blue, [0], 0, True)
        road(ans, i, red, blue, [0], 0, False)

    print(ans)


func9()
