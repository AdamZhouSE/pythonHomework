import collections


def dist(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])
    seen = {(sr, sc)}
    while queue:
        r, c, d = queue.popleft()
        if r == tr and c == tc:
            return d
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):
                seen.add((nr, nc))
                queue.append((nr, nc, d+1))
    return -1


def cutOffTree(forest):
    trees = sorted((v, r, c) for r, row in enumerate(forest)
                   for c, v in enumerate(row) if v > 1)
    sr = sc = ans = 0
    for _, tr, tc in trees:
        d = dist(forest, sr, sc, tr, tc)
        if d < 0: return -1
        ans += d
        sr, sc = tr, tc
    return ans


if __name__ == '__main__':
    matrix = []
    line = input()
    while line != "]":
        line = input()
        if len(line) > 1:
            t = []
            for i in range(0, len(line)):
                if line[i].isdecimal():
                    t.append(int(line[i]))
            matrix.append(t)
    print(cutOffTree(matrix))
