def n_again(source: str):
    for i in range(0, len(source)):
        if source.count(source[i]) > 1:
            return False
    return True


def func21():
    arr = eval(input())
    ans = 0
    left = 0
    for i in range(0, len(arr) + 1):
        sub = "".join(arr[left:i])
        if n_again(sub):
            ans = max(len(sub), ans)
        else:
            left += 1
    ans = max(ans, len("".join(arr[left:])))
    print(ans)
    


func21()
