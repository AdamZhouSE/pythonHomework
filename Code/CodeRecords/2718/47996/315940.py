import collections
def smallestStringWithSwaps(s, pairs):
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

str = input()
line = input()[1:-1].split("],")
pairs = []
for i in range(len(line)):
    if i != len(line)-1:
        temp = [int(x) for x in line[i][1:].split(",")]
        pairs.append(temp)
    else:
        temp = temp = [int(x) for x in line[i][1:-1].split(",")]
        pairs.append(temp)
print(smallestStringWithSwaps(str, pairs))
