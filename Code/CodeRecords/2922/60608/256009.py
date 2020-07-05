def func11():
    n = eval(input())
    arr = list(map(int, input().split()))
    val = max(arr)
    if min(arr) == val:
        print("YES")
    else:
        ans = False
        for i in range(0, n):
            if 2 * arr[i] == val - arr[i]:
                for j in range(0, n):
                    if arr[j] < 2 * arr[i] and arr[j] != arr[i]:
                        ans = False
                        break
                    if arr[j] > 2 * arr[i] and arr[j] != 3 * arr[i]:
                        ans = False
                        break
                    ans = True
        if ans:
            print("YES")
        else:
            print("NO")


func11()
