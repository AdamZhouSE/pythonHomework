
def func11():
    for _ in range(0, eval(input())):
        st = input()
        n = len(st)
        ans = -1
        for i in range(0, n - 1):
            for j in range(n - 1, i, -1):
                if st[i] == st[j]:
                    ans = max(ans, j - i - 1)
                    break
        print(ans)


func11()

