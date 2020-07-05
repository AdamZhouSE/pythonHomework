from collections import defaultdict
def removeStones(stones):
    """
    :type stones: List[List[int]]
    :rtype: int
    """

    def dfs(i, j):
        visited.add((i, j))
        for y in rows[i]:
            if (i, y) not in visited:
                dfs(i, y)
        for x in cols[j]:
            if (x, j) not in visited:
                dfs(x, j)

    visited, island, rows, cols = set(), 0, defaultdict(list), defaultdict(list)
    for i, j in stones:
        rows[i].append(j)
        cols[j].append(i)

    for i, j in stones:
        if (i, j) not in visited:
            dfs(i, j)
            island += 1

    return len(stones) - island


row=eval(input())
print(removeStones(row))