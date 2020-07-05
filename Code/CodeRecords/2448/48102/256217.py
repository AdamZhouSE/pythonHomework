def h_point(ls: list) -> int:
    ls.sort(reverse=True)
    for idx, item in enumerate(ls):
        if idx >= item:
            return idx
    return len(ls)


lst = eval(input())
print(h_point(lst))

