
def check(arr: list):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != 1:
            return False
    return True


def func28():
    for _ in range(0, eval(input())):
        n, arr, ans = eval(input()), sorted(list(map(int, input().split()))), 0
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                if check(sorted(arr[i:j])):
                    ans = max(ans, j - i)
        print(ans)


func28()
