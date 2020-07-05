def search(ls: list) -> list:
    from collections import defaultdict
    table = defaultdict(list)
    airports = defaultdict(int)
    res = []
    for x, y in ls:
        table[x].append(y)
        airports[x+y] += 1

    def dfs(i, temp, airport):
        nonlocal res
        if len(temp) == len(ls) + 1:
            res = temp
            return
        for j in sorted(table[i]):
            if airport[i+j] > 0 and not res:
                airport[i+j] -= 1
                dfs(j, temp + [j], airport)
                airport[i+j] += 1

    dfs('JFK', ['JFK'], airports)
    return res


lst = eval(input())
print(search(lst))