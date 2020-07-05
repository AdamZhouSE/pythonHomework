import sys
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

gcd = lambda a, b: b if not a % b else gcd(b, a % b)
no_gcd = lambda x, y: gcd(x, y) == 1 and gcd(x + 1, y + 1) == 1


def max_match(line, owned):
    def find(x):
        for want in line[x]:
            if not locked[want]:
                locked[want] = 1
                if owned[want] == -1 or find(owned[want]):
                    owned[want] = x
                    return True
        return False

    cnt = 0
    for i in range(len(line)):
        locked = [0] * len(owned)
        if find(i):
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = read()
    line = [[] for _ in range(n)]
    odd = []
    even = []
    for _ in range(n):
        v = read()
        (odd if v % 2 else even).append(v)
    line = [[] for _ in odd]
    for i, vi in enumerate(odd):
        for j, vj in enumerate(even):
            if no_gcd(vi, vj):
                line[i].append(j)
    r = max_match(line, [-1 for _ in even])
    print(n - r, end='')
