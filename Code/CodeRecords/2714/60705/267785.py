# 不会写

def f(a: str, b: str)->bool:
    if not (len(b) == len(a) + 1):
        return False
    for i in a:
        if not b.count(i) >= a.count(i):
            return False
    return True


if __name__ == '__main__':
    li = []
    while True:
        try:
            li.append(input())
        except EOFError:
            break
    li = sorted(li, key=lambda k: len(k))
    res_list = [li[0]]
    current = li[0]
    for i in range(1, len(li)):
        if f(current, li[i]):
            current = li[i]
            res_list.append(current)
    print(res_list)
