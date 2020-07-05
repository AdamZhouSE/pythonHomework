
def func22():
    for _ in range(0, eval(input())):
        n, ans, t, res = eval(input()), [], 1, 6
        while res <= n:
            if res == n:
                for i in range(0, 3):
                    ans.append(t + i)
                break
            else:
                t += 1
                res = 3*t+3
                
        if not ans:
            print(-1)
        else:
            for i in range(0, 2):
                print(ans[i], end=" ")
            print(ans[-1])


func22()
