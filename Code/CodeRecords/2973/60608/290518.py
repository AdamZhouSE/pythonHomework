
def func9():
    source, n = list(input()), eval(input())
    val, arr = 0, []
    for i in range(0, n):
        arr.append(input())
    for i in range(0, n):
        s, res = set(arr[i]), {}
        for j in s:
            res[j] = arr[i].count(j)
        for j in range(0, len(source) - 7):
            t = source[j:j + 8]
            if set(t) == s:
                flag = True
                for k in s:
                    if t.count(k) != res[k]:
                        flag = False
                        break
                if flag:
                    val += 1
    print(val)


func9()