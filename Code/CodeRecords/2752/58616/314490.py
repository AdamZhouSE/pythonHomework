# LeetCode 675
class Solution:
    def cutOffTree(self, forest):
        row = len(forest)
        col = len(forest[0])
        arr = []
        for i in range(row):
            for j in range(col):
                if forest[i][j]:
                    arr.append([i,j,forest[i][j]])
        arr.sort(key=lambda x: x[2])
        def bfs(i,j,r,c):
            q = [(i,j,0)]
            seen = {(i,j)}
            while q:
                i,j,step = q.pop(0)
                if (i,j) == (r,c):
                    return step
                for ti,tj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=ti<row and 0<=tj<col and (ti,tj) not in seen and forest[ti][tj]:
                        seen.add((ti,tj))
                        q.append((ti,tj,step+1))
            return -1
        res = i = j = 0
        for r,c,_ in arr:
            step = bfs(i,j,r,c)
            if step == -1:
                return -1
            res += step
            i,j = r,c
        return res


matrix = []
while True:
    test = input()
    if test == "[":
        continue
    elif test == "]":
        break
    else:
        if test[-1] == ",":
            test = test[:len(test) - 1]
        line = eval(test)
        matrix.append(line)
s = Solution()
print(s.cutOffTree(matrix))