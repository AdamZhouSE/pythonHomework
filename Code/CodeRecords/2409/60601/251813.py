def minCostToMoveChips(chips:list) -> int:
    res = [0, 0]
    for c in chips:
        res[c % 2] += 1
    return min(res)
chips = list(map(int,input().split(',')))
print(minCostToMoveChips(chips))