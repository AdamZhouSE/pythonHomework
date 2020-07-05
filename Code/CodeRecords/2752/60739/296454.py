# 为高尔夫比赛砍树
import collections

def getInput(input_str):
    nums_str1 = input_str.replace(' ', '')
    nums_str1 = nums_str1.replace('[', '')
    nums_str1 = nums_str1.replace(']', '')
    if nums_str1[-1] == ',':
        nums_str1 = nums_str1[0:len(nums_str1) - 1];

    nums = [int(n) for n in nums_str1.split(",")];
    return nums;


def cutOffTree(forest):
    trees = sorted((v, r, c) for r, row in enumerate(forest)
                   for c, v in enumerate(row) if v > 1)
    sr = sc = ans = 0
    for _, tr, tc in trees:
        d = bfs(forest, sr, sc, tr, tc)
        if d < 0: return -1
        ans += d
        sr, sc = tr, tc
    return ans

def bfs(forest, sr, sc, tr, tc):
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


l = input()
l = input()
matrix = []
while l != ']':
    matrix.append(getInput(l))
    l = input()
print(cutOffTree(matrix))
