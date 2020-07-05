def string_sort(string: str) -> list:
    res = []
    for i in range(len(string)):
        res.append(string[i:])
    res.sort()
    lst = []
    for i in res:
        lst.append(len(string)-len(i)+1)
    return lst


s = input()
ans = string_sort(s)
for k in range(len(ans)-1):
    print(str(ans[k]) + ' ', end='')
print(ans[len(ans)-1])