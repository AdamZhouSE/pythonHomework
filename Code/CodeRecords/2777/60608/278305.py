
def func24():
    for _ in range(0, eval(input())):
        n, arr = eval(input()), sorted(list(map(int, input().split())))
        left, right = 0, n - 1
        while right - left > 1:
            left += 1
            right -= 1
        print(arr[left] if left == right else (arr[left] + arr[right]) // 2)


func24()