def func9():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        ans = [1,2]
        while n > len(ans):
            ans.append(ans[len(ans)-1]+ans[len(ans)-2])
        print(ans[n-1])
    return
func9()