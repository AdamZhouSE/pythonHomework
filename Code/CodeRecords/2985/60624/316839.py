def func7():
    ans = ["A"]
    for i in range(1,26):
        ans.append(ans[i-1] + chr(ord("A")+i) + ans[i-1])
    n = int(input())
    print(ans[n-1])
    return
func7()