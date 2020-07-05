
def func27():
    for _ in range(0, eval(input())):
        n, arr, k, ans = eval(input()), list(map(int, input().split())), eval(input()), 1
        for i in range(0, n):
            ans *= arr[i]
        print(ans % k)


func27()