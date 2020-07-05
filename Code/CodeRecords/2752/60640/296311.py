import re


class Solution:
    def cutOffTree(self, forest) -> int:
        row = len(forest)
        col = len(forest[0])
        arr = []
        for i in range(row):
            for j in range(col):
                if forest[i][j]:
                    arr.append([i, j, forest[i][j]])
        arr.sort(key=lambda x: x[2])

        def bfs(i, j, r, c):
            q = [(i, j, 0)]
            seen = {(i, j)}
            while q:
                i, j, step = q.pop(0)
                if (i, j) == (r, c):
                    return step
                for ti, tj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ti < row and 0 <= tj < col and (ti, tj) not in seen and forest[ti][tj]:
                        seen.add((ti, tj))
                        q.append((ti, tj, step + 1))
            return -1

        res = i = j = 0
        for r, c, _ in arr:
            step = bfs(i, j, r, c)
            if step == -1:
                return -1
            res += step
            i, j = r, c
        return res


if __name__ == "__main__":
    symbol = input()
    arr = []
    while True:
        inp = input()
        if inp == "]":
            break
        row = re.split(r"[\[\]\",]", inp)
        while "" in row:
            row.remove("")
        while " " in row:
            row.remove(" ")
        row = [int(x) for x in row]
        arr.append(row)
    s = Solution()
    res = s.cutOffTree(arr)
    print(res)
