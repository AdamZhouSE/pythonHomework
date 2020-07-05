class Plane(object):
    def __init__(self):
        self.time = 0
        self.value = 0

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.time < other.time:
                return True
            else:
                return False
        else:
            return False


class Tree(object):
    def __init__(self):
        self.left = 0
        self.right = 0
        self.flag = False


def build(p: int, left: int, right: int):
    global trees
    trees[p].left = left
    trees[p].right = right
    if trees[p].left == trees[p].right:
        return
    mid = (left + right) >> 1
    build(p << 1, left, mid)
    build(p << 1 | 1, mid+1, right)


def query(p: int, x: int) -> int:
    global trees
    if trees[p].left == trees[p].right:
        return trees[p].left
    mid = (trees[p].left + trees[p].right) >> 1
    if not trees[p << 1].flag and x <= mid:
        return query(p << 1, x)
    else:
        return query(p << 1 | 1, x)


def push_up(p: int):
    global trees
    trees[p].flag = trees[p << 1].flag and trees[p << 1 | 1].flag


def update(p: int, x: int):
    global trees
    if trees[p].left == trees[p].right:
        trees[p].flag = True
        return
    mid = (trees[p].left + trees[p].right) >> 1
    if x <= mid:
        update(p << 1, x)
    else:
        update(p << 1 | 1, x)
    push_up(p)


if __name__ == '__main__':
    temp1 = input().split(' ')
    temp1 = list(map(int, temp1))

    n, k = temp1[0], temp1[1]
    planes = [Plane() for _ in range(n+1)]
    trees = [Tree() for _ in range((n+1) << 2)]
    ans = [0 for _ in range(n+1)]
    sum_cost = 0

    temp2 = input().split(' ')
    temp2 = list(map(int, temp2))
    for i in range(1, n+1):
        planes[i].time = i
        planes[i].value = temp2[i-1]
    planes.sort(reverse=True)
    planes.remove(planes[n])
    planes.insert(0, Plane())

    build(1, 1, n)

    for i in range(1, n+1):
        t = query(1, max(planes[i].time - k, 1))
        ans[planes[i].time] = t + k
        sum_cost += (t + k - planes[i].time) * planes[i].value
        update(1, t)

    print(sum_cost)
    for i in range(1, n+1):
        print('{0} '.format(ans[i]), end='')
    print()
