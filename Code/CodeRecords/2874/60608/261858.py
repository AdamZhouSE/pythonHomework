def func36():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = 0
    res = 0
    for i in range(0, n):
        if arr[i] == 0:
            res = 0
            ans += 1
        elif arr[i] == 1:
            if res == 1:
                res = 0
                ans += 1
            else:
                res = 1
        elif arr[i] == 2:
            if res == 2:
                res = 0
                ans += 1
            else:
                res = 2
        else:
            if res == 1:
                res = 2
            elif res == 2:
                res = 1
            else:
                counter = 0
                while arr[i + counter] == 3:
                    counter += 1
                if arr[i + counter] == 0:
                    res = 1
                elif arr[i + counter] == 1:
                    res = 1 if counter % 2 == 0 else 2
                else:
                    res = 2 if counter % 2 == 0 else 1
    print(ans)
    


func36()
