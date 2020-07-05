sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())


def dfs(x, y):
    if x == tx and y == ty:
        return True
    elif x > tx or y > ty:
        return False
    else:
        if dfs(x + y, y):
            return True
        if dfs(x, x + y):
            return True
    return False


print(dfs(sx, sy))