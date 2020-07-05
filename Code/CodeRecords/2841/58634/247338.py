# 奇数次是或，偶数次是异或
# 线段树，叶节点是原始数组

def build(left, right, root, judge):
    global a
    global sum_
    if left == right:
        sum_[root] = a[left]  # 最后一个叶节点不做or和xor的处理,递归出口
        return
    middle = (left + right) // 2
    build(left, middle, root * 2, 1 - judge)
    build(middle + 1, right, root * 2+1, 1 - judge)
    if judge == 1:
        sum_[root] = sum_[root * 2] | sum_[root * 2 + 1]
    else:
        sum_[root] = sum_[root * 2] ^ sum_[root * 2 + 1]


def update(p, left, right, root, b, judge):
    global a
    global sum_
    if (left == right):
        sum_[root] = b
        return
    mid = (left + right) >> 1
    if p > mid:
        update(p, mid + 1, right, root * 2 + 1, b, 1 - judge)
    else:
        update(p, left, mid, root * 2, b, 1 - judge)
    if judge == 1:
        sum_[root] = sum_[root * 2] | sum_[root * 2 + 1]
    else:
        sum_[root] = sum_[root * 2] ^ sum_[root * 2 + 1]


n, m = map(int, input().split())
length = 1 << n
a = [int(i) for i in input().split(" ")]
sum_ = [0] * (1 << 17)
a.insert(0, 0)  # 在起始点插入一个无效元素，从1开始计算
build(1, length, 1, n % 2)
for i in range(m):
    p, b = map(int, input().split())
    update(p, 1, length, 1, b, n % 2)
    print(sum_[1])
