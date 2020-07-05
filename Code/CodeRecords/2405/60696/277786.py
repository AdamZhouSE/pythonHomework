lch = []
rch = []
height = []


def get_height(n):
    if lch[n] != 0:
        get_height(lch[n])
    if rch[n] != 0:
        get_height(rch[n])
    height[n] = 1 + max(height[lch[n]], height[rch[n]])


def get_width(n):
    stack = [n]
    width = 0
    while len(stack) != 0:
        width = max(width, len(stack))
        temp = []
        for each in stack:
            if lch[each] != 0:
                temp.append(lch[each])
            if rch[each] != 0:
                temp.append(rch[each])
        stack = temp
    return width


def get_least__common_ancestor(root, p, q):
    if root == 0 or root == p or root == q:
        return root
    left = get_least__common_ancestor(lch[root], p, q)
    right = get_least__common_ancestor(rch[root], p, q)
    if left != 0 and right != 0:
        return root
    if left != 0:
        return left
    else:
        return right


if __name__ == '__main__':
    n = int(input())
    lch = [0 for i in range(n+1)]
    rch = [0 for i in range(n+1)]
    height = [0 for i in range(n+1)]
    for i in range(n-1):
        arr = [int(j) for j in input().split()]
        if lch[arr[0]] == 0:
            lch[arr[0]] = arr[1]
        else:
            rch[arr[0]] = arr[1]
    arr = [int(i) for i in input().split()]
    p = arr[0]
    q = arr[1]
    least_ancestor = get_least__common_ancestor(1, p, q)
    get_height(1)
    distance = 2 * (height[least_ancestor] - height[p]) + height[least_ancestor] - height[q]
    print(height[1])
    print(get_width(1))
    print(distance)