# 如题，一开始有N个小根堆，每个堆包含且仅包含一个数。接下来需要支持两种操作：
#
# 操作1： 1 x y 将第x个数和第y个数所在的小根堆合并（若第x或第y个数已经被删除或第x和第y个数在用一个堆内，则无视此操作）
#
# 操作2： 2 x 输出第x个数所在的堆最小数，并将其删除（若第x个数已经被删除，则输出-1并无视删除操作）

import heapq

def delete(heaps: [[int]], x: int, deleted: [int]):
    where = x
    deleted.append(x)
    # print("To delete:", heaps[where])
    del heaps[where][0] # 第一个数为0，即说明已经被删除
    heapq.heapify(heaps[where])

# 返回的是位置
def findHeap(heaps: [[int]], x: int) -> int:
    begin = x-1
    while heaps[begin][0] < 0:
        begin = -heaps[begin][0]
    return begin

# 合并，输入的是序号
def merge(heaps: [[int]], x1: int, x2: int):
    h1 = heaps[x1]
    h2 = heaps[x2]
    h2 = h1+h2
    heapq.heapify(h2)
    # print(h2)
    heaps[x2] = h2
    heaps[x1][0] = -x2

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    x = input().strip().split()
    heaps = []
    for i in range(n):
        heaps.append([int(x[i])])
    ops = []
    deleted = []
    for i in range(m):
        ops.append(input())
    for op in ops:
        op = op.strip().split()
        if op[0] == "1": # 1 x y 将第x个数和第y个数所在的小根堆合并（若第x或第y个数已经被删除或第x和第y个数在用一个堆内，则无视此操作）
            # print(heaps)
            if int(op[1]) in deleted or int(op[2]) in deleted:
                continue
            h1 = findHeap(heaps, int(op[1]))
            h2 = findHeap(heaps, int(op[2]))
            if h1 == h2:
                continue
            merge(heaps, h1, h2)
        else: # 2 x 输出第x个数所在的堆最小数，并将其删除（若第x个数已经被删除，则输出-1并无视删除操作）
            h0 = findHeap(heaps, int(op[1]))
            if heaps[h0][0] == 0:
                print("-1")
            else:
                xx = heaps[h0][0]
                delete(heaps, h0, deleted)
                print(xx)


