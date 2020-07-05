def func6():
    n = int(input())
    k = int(input())
    if n == 1:
        print("".join(str(i) for i in range(k)))
    else:
        temp, ans = {}, "0" * (n-1)
        for i in range(k ** n):
            j = ans[1-n]
            temp[j] = temp.get(j, k) - 1
            ans += str(temp[j])
        print(ans)
    return
func6()