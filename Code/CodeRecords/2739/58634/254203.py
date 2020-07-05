def combinationSum(target, index, path, res, k):
    if target == 0 and len(path) == k:
        res.append(path)
        return

    if path and target < path[-1]:
        return

    for i in range(index, 10):
        combinationSum(target - i, i + 1, path + [i], res, k)



k, n = map(int, input().split(","))
result = []
combinationSum(n, 1, list(), result, k)
print(result)