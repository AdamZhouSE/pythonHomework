lch = []
rch = []


def least_common_ancestor(root, p, q):
    if root == p or root == q or root == 0:
        return root
    left = least_common_ancestor(lch[root], p, q)
    right = least_common_ancestor(rch[root], p, q)
    if left == 0:
        return right
    if right == 0:
        return left
    else:
        return root


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    root = arr[1]
    lch = [0 for i in range(n+1)]
    rch = [0 for i in range(n+1)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        lch[arr[0]] = arr[1]
        rch[arr[0]] = arr[2]
    m = int(input())
    for i in range(m):
        arr = [int(j) for j in input().split()]
        p = arr[0]
        q = arr[1]
        print(least_common_ancestor(root, p, q))
