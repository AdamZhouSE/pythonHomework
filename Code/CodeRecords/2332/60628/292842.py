import math
def leastOperations(x, target):
    k = int(math.log(target, x)) + 1

    def dfs(y, k):
        if k == 0:
            return y + y - 1
        elif y == 0:
            return -1
        need, left = divmod(y, x ** k)
        return min(dfs(left, k - 1) + need * k, dfs(x ** k - left, k - 1) + (need + 1) * k)

    return dfs(target, k)

x = int(input())
target = int(input())
print(leastOperations(x, target))