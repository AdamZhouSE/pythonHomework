n, m, q = list(map(int, input().split()))
visited = []
person = [0 for i in range(n)]
for i in range(q):
    a, b, c = input().split()
    if a == "C":
        person[int(b) - 1] = int(c) - 1
    if a == "W":
        res = 0
        for r in range(int(b) - 1, int(c)):
            ps = []
            for p in range(len(person)):
                if person[p] == r:
                    ps.append(p)
            if ps not in visited:
                res += len(ps)
                visited.append(ps)
            else:
                res += 0
        print(res)
