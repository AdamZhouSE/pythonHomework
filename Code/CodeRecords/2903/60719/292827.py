def str_to_list(l, split):
    l0 = l[1: len(l)-1].split(split)
    return l0


def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x

def dfs(cur, arr, m):
    if cur >= len(arr):
        return 0
    t = m.copy()
    for i in range(len(arr)):
        uf = ord(arr[cur][i]) - ord("a")
        if uf != 0:
            return dfs(cur+1, arr, m)
        t[uf] += 1
    len1 = len(arr[cur]) + dfs(cur+1, arr, t)
    len2 = dfs(cur+1, arr, m)
    return max(len1, len2)


s = str_to_list(input().replace('"', ""), ",")
m = [0]*27
l = dfs(0, s, m)
print(l)