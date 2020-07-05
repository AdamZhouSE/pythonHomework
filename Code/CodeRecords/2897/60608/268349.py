def word(s1: str, s2: str):
    set1 = set(list(s1))
    set2 = set(list(s2))
    if not set1 & set2:
        return len(s1) * len(s2)
    return 0


def func8():
    arr = eval(input())
    ans = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            ans = max(ans, word(arr[i], arr[j]))
    print(ans)


func8()
