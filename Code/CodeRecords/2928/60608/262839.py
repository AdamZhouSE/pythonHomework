def fetch(num: int, tem: list, val: int, least: int):
    for item in tem:
        if num >= item[1] and (num - item[1]) // least == val:
            return item


def func44():
    v = eval(input())
    arr = list(map(int, input().split()))
    res = {}
    for i in range(0, 9):
        res[i + 1] = arr[i]
    tem = sorted(res.items(), key=lambda x: -x[0])
    ans = []
    val = v // min(res.values())
    least = min(res.values())

    while v >= least:
        val -= 1
        t = fetch(v, tem, val, least)
        v -= t[1]
        ans.append(t[0])

    if ans:
        print("".join(list(map(str, sorted(ans, reverse=True)))))
    else:
        print(-1)


func44()
