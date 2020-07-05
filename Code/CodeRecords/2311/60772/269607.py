def func(d):
    if len(d) == 1:
        return [0]
    elif len(d) == 0:
        return []
    mid = len(d) // 2  # 满二叉树根节点即正中间数值，前序遍历数组本题中用不到，可删除
    return func(d[:mid]) + [sum(d[:]) - d[mid]] + func(d[mid + 1:])


if __name__ == "__main__":
    a = list(map(int, input().strip().split()))
    d = list(map(int, input().strip().split()))
    ans = func(d)
    print(' '.join(map(str, ans)),end=" ")