class Edge(object):
    def __init__(self, left: int, right: int, station: int, age: int):
        self.left = left
        self.right = right
        self.station = station
        self.age = age


def build(p: int, left: int, right: int):
    global t
    t[p].left = left
    t[p].right = right
    t[p].station = 2**31-1
    if left == right:
        t[p].age = left
        return
    mid = (left + right) >> 1
    build(p << 1, left, mid)
    build(p << 1 | 1, mid+1, right)


def push_up(p: int):
    global t
    if t[p << 1].station < t[p << 1 | 1].station:
        t[p].station = t[p << 1].station
        t[p].age = t[p << 1].age
    else:
        t[p].station = t[p << 1 | 1].station
        t[p].age = t[p << 1 | 1].age


def update(p: int, age: int, station: int):
    global t
    if t[p].left == t[p].right:
        t[p].station = min(t[p].station, station)
        return
    mid = (t[p].left + t[p].right) >> 1
    if mid >= age:
        update(p << 1, age, station)
    else:
        update(p << 1 | 1, age, station)
    push_up(p)


def query(p: int, left: int, right: int, station: int) -> list:
    global t
    if t[p].left == t[p].right:
        return [t[p].station, t[p].age]
    if left <= t[p].left and t[p].right <= right:
        if t[p].station <= station:
            if t[p << 1].station <= station:
                return query(p << 1, left, right, station)
            else:
                return query(p << 1 | 1, left, right, station)
        else:
            return [2**31-1, 0]
    mid = (t[p].left + t[p].right) >> 1
    ans = [2**31-1, 0]
    if left <= mid:
        ans = query(p << 1, left, right, station)
        if ans[0] <= station:
            return ans
    if right > mid:
        ans = query(p << 1 | 1, left, right, station)
        if ans[0] <= station:
            return ans
    return ans


if __name__ == '__main__':
    t = [Edge(0, 0, 0, 0) for _ in range(800010)]
    temp1 = input().split(' ')
    temp1 = list(map(int, temp1))
    n = temp1[0]
    q = temp1[1]
    build(1, 1, n)
    final = []
    for _ in range(q):
        temp2 = input().split(' ')
        if temp2[0] == 'M':
            update(1, int(temp2[2]), int(temp2[1]))
        if temp2[0] == 'D':
            res = query(1, int(temp2[2]), n, int(temp2[1]))
            if res[0] > int(temp2[1]):
                final.append(-1)
            else:
                final.append(res[1])
    for k in final:
        print(k)