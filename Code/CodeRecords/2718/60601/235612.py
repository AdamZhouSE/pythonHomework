import collections


def solve(s,pairs):
    p = list(range(len(s)))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    for i, j in pairs:
        px, py = find(i), find(j)
        if px != py:
            p[px] = py

    mem = collections.defaultdict(list)
    for i, v in enumerate(p):
        mem[find(v)].append(s[i])
    for k in mem:
        mem[k].sort(reverse=True)

    res = []
    for i in range(len(s)):
        res.append(mem[find(i)].pop())
    return "".join(res)


if __name__ == '__main__':
    str = input()
    line = input()
    line = line[2:len(line)-2]
    line = line.split('],[')
    for i in range(len(line)):
        line[i] = line[i].replace(',',' ')
        line[i] = list(map(int,line[i].split()))
    print(solve(str,line))