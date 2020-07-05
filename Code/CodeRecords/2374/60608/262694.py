def func42():
    for _ in range(0, eval(input())):
        n = eval(input())
        arr = list(map(int, input().split()))
        res = {}
        for i in range(0, n):
            if arr[i] in res.keys():
                res[arr[i]] += 1
            else:
                res[arr[i]] = 1
        res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
        ans = []

        for i in range(0, len(res)):
            ans += [res[i][0] for j in range(0, res[i][1])]
        for i in range(0, len(ans) ):
            print(ans[i], end=" ")
        print()


func42()
