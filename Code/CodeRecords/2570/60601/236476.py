from bisect import bisect_left

def solve(envelopes: list):
    if not envelopes:
        return 0

    res, n = 0, len(envelopes)
    envelopes.sort(key=lambda a: (a[0], -a[1]))
    mem = list()
    for e in envelopes:
        index = bisect_left(mem, e[1])
        if len(mem) == index:
            mem.append(e[1])
        else:
            mem[index] = e[1]
    return len(mem)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
         arr.append(list(map(int,input().split(','))))
    #print(arr)
    print(solve(arr))
