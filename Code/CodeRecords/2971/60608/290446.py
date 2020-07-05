
def func8():
    chars: int = input()
    res = []
    for i in range(0, len(chars)):
        res.append((chars[i:], i))
    res = sorted(res, key=lambda x: x[0])
    for t in res:
        print(t[1] + 1, end=' ')


func8()