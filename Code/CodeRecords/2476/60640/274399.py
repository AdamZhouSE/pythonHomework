"""
采用最小堆
每次取出最小堆中最小的两个元素相加并重新加入堆中
重复上述步骤直到堆中只剩下一个元素
"""


def heap(arr):
    ans = 0
    while len(arr) > 1:
        min1 = arr.pop()
        min2 = arr.pop()
        ans += min1+min2
        arr.append(min1+min2)
        arr.sort(reverse=True)
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    # 降序排序，形成最小堆
    inp.sort(reverse=True)
    res = heap(inp)
    print(res)
