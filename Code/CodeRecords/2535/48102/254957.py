def sort_str(arr: list) -> int:
    ans = ma = 0
    for i, x in enumerate(arr):
        ma = max(ma, x)
        if ma == i:
            ans += 1
    return ans


lst = eval(input())
print(sort_str(lst))