def func7():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        ans = [1]
        length = 1
        while n > length:
            length += 1
            ans.append((ans[length-2]+1) % length+1)
        print(ans[n-1])
    return
func7()