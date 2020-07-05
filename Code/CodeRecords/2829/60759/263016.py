def stable():
    if len(lst) <= 2:
        return 0
    max_n, min_n = max(lst), min(lst)
    lst.pop()
    lst.pop(0)
    return min(max_n - lst[0], lst[len(lst) - 1] - min_n)


n = int(input())
lst = sorted(list(map(int, input().split(' '))))
print(stable())
