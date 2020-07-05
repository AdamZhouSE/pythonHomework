

def func8():
    for _ in range(0, eval(input())):
        n, arr = eval(input()), list(map(int, input().split()))
        if arr.count(0) > 0:
            print("Yes")
        else:
            ans = "No"
            for i in range(0, n):
                for j in range(i + 1, n + 1):
                    if sum(arr[i:j]) == 0:
                        ans = "Yes"
                        break
                if ans == "Yes":
                    break
            print(ans)


func8()
