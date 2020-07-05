def solve(s, k):
    s = list(s)
    result = 0
    for ii in range(len(s)):
        collect = set()
        for jj in range(ii, len(s)):
            if s[jj] not in collect:
                collect.add(s[jj])
            if len(collect) == k:
                result = max(result, jj - ii + 1)
    return result


T = int(input())
for ttt in range(T):
    print(solve(input().strip(), int(input())))
