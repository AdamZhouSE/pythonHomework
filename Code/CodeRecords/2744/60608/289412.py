
def check(word: str):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        right -= 1
        left += 1
    return True


def func26():
    n: int = eval(input())
    res, ans = [], 0
    for i in range(0, n):
        res.append(input().split()[1])
    for i in range(0, n):
        for j in range(0, n):
            if check(res[i] + res[j]):
                ans += 1
    print(ans)


func26()
