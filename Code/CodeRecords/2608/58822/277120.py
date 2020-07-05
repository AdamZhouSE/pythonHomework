yuanyin = ['a', 'e', 'i', 'o', 'u']


def dfs(s):
    if len(s) == 1:
        return ['', s]
    p1 = dfs(s[:-1])
    p2 = []
    for tmp in p1:
        if tmp == '' or tmp[0] in yuanyin:
            p2.append(tmp + s[-1])
    return p1 + p2


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        results = list(filter(lambda x: len(x) > 1 and not x[-1] in yuanyin, dfs(s)))
        if len(results) == 0:
            print(-1)
            continue
        distinct_results = []
        for r in results:
            if not r in distinct_results:
                distinct_results.append(r)
        distinct_results.sort()
        print(' '.join(distinct_results))
