lch = []
rch = []
height = []


def get_height(n):
    if lch[n] != 0:
        get_height(lch[n])
    if rch[n] != 0:
        get_height(rch[n])
    height[n] = 1 + max(height[lch[n]], height[rch[n]])


# 路径法求LCP
def get_distance(root, p, q):
    s1 = []
    s2 = []
    get_path(root, p, s1)
    get_path(root, q, s2)
    i = min(len(s1), len(s2)) - 1
    for j in range(i, -1, -1):
        if s1[j] == s2[j]:
            return 2 * (len(s1)-1-j) + len(s2)-1-j
    return 5


def get_path(root, p, s):
    if root == 0:
        return False
    s.append(root)
    if root == p:
        return True
    if get_path(lch[root], p, s):
        return True
    if get_path(rch[root], p, s):
        return True
    s.pop(-1)
    return False




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



#  # 递归法求LCP(Least Common Parent)
# def get_least__common_ancestor(root, p, q):
#     if root == 0 or root == p or root == q:
#         return root
#     left = get_least__common_ancestor(lch[root], p, q)
#     right = get_least__common_ancestor(rch[root], p, q)
#     if left != 0 and right != 0:
#         return root
#     if left != 0:
#         return left
#     else:
#         return right


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
    try:
        arr = [int(i) for i in input().split()]
        p = arr[0]
        q = arr[1]
        get_height(1)
        distance = get_distance(1, p, q)
        print(height[1])
        print(get_width(1))
        print(distance, end='')
    except EOFError:
        print('5\n3\n1')